from app.ml.model_config import model_config
from app.ml.model_pipelines import Log1pImputer, RatioInteractionImputer  # noqa: F401
from pathlib import Path
import pickle


class MlProcessor:

    def __init__(self):
        self.models_path = Path(__file__).resolve().parent.parent / "ml" / "models"
        self.model_name = model_config.MODEL_NAME
        self.model_score_threshold = model_config.MODEL_SCORE_THRESHOLD
        self.model = self.__load_model()

    def __load_model(self):
        try:
            model = pickle.load(open(self.models_path / self.model_name, "rb"))
        except Exception as e:
            raise Exception(
                f"Cannot load the model! model_name: {self.model_name}, model_path: {self.models_path}. ERROR: {e}"
            )

        return model

    def score_single(self, features):
        return self.model.predict_proba(features)[:, 1][0]


ml_processor = MlProcessor()
