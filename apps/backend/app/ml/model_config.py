from pydantic_settings import BaseSettings


class ModelConfig(BaseSettings):
    MODEL_NAME: str = "log_reg_pipeline_without_outliers_v2.pkl"
    APPROVE_THRESHOLD: float = 0.85
    REVIEW_THRESHOLD: float = 0.60  # Below this -> reject
    NUMBER_OF_CONTRIBUTORS: int = 5


model_config = ModelConfig()
