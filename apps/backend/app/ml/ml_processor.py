from pathlib import Path
import pandas as pd
import numpy as np
import pickle
from typing import Tuple

from app.ml import model_pipelines
from app.ml.model_config import model_config
from app.models.ml_models import Contributors, ModelSignals

# Pickles saved from a notebook/script register custom steps as __main__.ClassName;
# at runtime __main__ is uvicorn, so unpickling fails unless we remap to real modules.
_MAIN_CLASS_ALIASES = {
    "Log1pImputer": model_pipelines.Log1pImputer,
    "RatioInteractionImputer": model_pipelines.RatioInteractionImputer,
}


class _PipelineUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__" and name in _MAIN_CLASS_ALIASES:
            return _MAIN_CLASS_ALIASES[name]
        return super().find_class(module, name)


class MlProcessor:

    def __init__(self):
        self.models_path = Path(__file__).resolve().parent.parent / "ml" / "models"
        self.model_name = model_config.MODEL_NAME
        self.model = self.__load_model()
        self.n_contributors = model_config.NUMBER_OF_CONTRIBUTORS

    def __load_model(self):
        try:
            path = self.models_path / self.model_name
            with open(path, "rb") as f:
                model = _PipelineUnpickler(f).load()
        except Exception as e:
            raise Exception(
                f"Cannot load the model! model_name: {self.model_name}, model_path: {self.models_path}. ERROR: {e}"
            )

        return model

    def score_single(self, features: pd.DataFrame) -> Tuple[float, ModelSignals]:
        model_signals = self.__get_contributors(features)
        score = self.model.predict_proba(features)[:, 1][0]

        return score, model_signals

    def __get_contributors(self, features: pd.DataFrame):
        preprocessor = self.model[:-1]
        model = self.model[-1]

        Xt = preprocessor.transform(features)
        feature_names = preprocessor.get_feature_names_out()

        if hasattr(Xt, "toarray"):
            Xt = Xt.toarray()

        x = Xt[0]

        coef = model.coef_[0]
        contributions = x * coef

        order = np.argsort(contributions)
        top_idx = order[-self.n_contributors :]
        bottom_idx = order[: self.n_contributors]

        top_contributors = Contributors(
            featureNames=feature_names[top_idx], contribution=contributions[top_idx]
        )

        bottom_contributors = Contributors(
            featureNames=feature_names[bottom_idx],
            contribution=contributions[bottom_idx],
        )

        return ModelSignals(
            topPositive=top_contributors, topNegative=bottom_contributors
        )


ml_processor = MlProcessor()
