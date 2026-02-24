from fastapi import FastAPI
from app.core.settings import settings
from app.core.logging_config import LoggingConfig, get_logger

logging_config = LoggingConfig(log_level=settings.LOG_LEVEL, log_dir=settings.LOG_DIR)
logger = get_logger(__name__)


def create_app() -> FastAPI:

    logger.info(f"Setting up the {settings.PROJECT_NAME} app...")
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    # TODO: setup middleware!

    # Including routers

    logger.info(f"Setting up the {settings.PROJECT_NAME} app done.")
    return app


app = create_app()


@app.get("/")
def root():
    return {"Info": f"{settings.PROJECT_NAME} version: {settings.VERSION} backend app"}


@app.get("/health")
def health():
    return {"status": "ok"}
