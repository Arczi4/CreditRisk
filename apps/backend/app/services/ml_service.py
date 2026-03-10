from app.ml.model_config import model_config
from pathlib import Path
import pickle


class MlService:

    def __init__(self):
        self.models_path = Path("app", "ml", "models")
        self.model_name = model_config.MODEL_NAME
        self.model_score_threshold = model_config.MODEL_SCORE_THRESHOLD
        self.model = self.__load_model()

    def __load_model(self):
        model = pickle.load(self.models_path / self.model_name)

        return model


ml_service = MlService()

print(ml_service)
