from pathlib import Path
import pandas as pd
import numpy as np
import pickle
from typing import Tuple

from app.ml.model_config import model_config
from app.ml.model_pipelines import Log1pImputer, RatioInteractionImputer  # noqa: F401
from app.models.ml_models import Contributors, ModelSignals


class MlProcessor:

    def __init__(self):
        self.models_path = Path(__file__).resolve().parent.parent / "ml" / "models"
        self.model_name = model_config.MODEL_NAME
        self.model = self.__load_model()
        self.n_contributors = model_config.NUMBER_OF_CONTRIBUTORS

    def __load_model(self):
        try:
            model = pickle.load(open(self.models_path / self.model_name, "rb"))
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
