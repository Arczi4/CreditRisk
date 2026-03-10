from app.ml.model_config import model_config
from app.ml.model_pipelines import Log1pImputer, RatioInteractionImputer  # noqa: F401
from pathlib import Path
import pickle


class MlService:

    def __init__(self):
        self.models_path = Path("app", "ml", "models")
        self.model_name = model_config.MODEL_NAME
        self.model_score_threshold = model_config.MODEL_SCORE_THRESHOLD
        self.model = self.__load_model()

    def __load_model(self):
        model = pickle.load(open(self.models_path / self.model_name, "rb"))

        return model


ml_service = MlService()
