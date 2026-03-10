from pydantic_settings import BaseSettings


class ModelConfig(BaseSettings):
    MODEL_NAME: str = "log_reg_without_outliers.pkl"
    MODEL_SCORE_THRESHOLD: float = 0.85


model_config = ModelConfig()
