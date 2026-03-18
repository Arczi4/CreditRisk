from pydantic_settings import BaseSettings


class ModelConfig(BaseSettings):
    MODEL_NAME: str = "log_reg_without_outliers.pkl"
    APPROVE_THRESHOLD: float = 0.85
    REVIEW_THRESHOLD: float = 0.60  # Below this -> reject


model_config = ModelConfig()
