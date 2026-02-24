from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "CreditRisk"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"

    # Server Config
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # Cors config
    CORS_ORIGIN: str = "http://localhost:4200"  # Default angular

    # Logging config
    LOG_DIR: str = "logs"

    @property
    def LOG_LEVEL(self) -> str:
        return "debug" if self.DEBUG else "info"


settings = Settings()
