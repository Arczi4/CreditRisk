from pydantic_settings import BaseSettings


class ModelConfig(BaseSettings):
    MODEL_NAME = "log_reg_without_outliers.pkl"
    MODEL_SCORE_THRESHOLD = 0.85


model_config = ModelConfig()
