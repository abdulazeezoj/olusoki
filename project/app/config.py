import logging
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False


def get_settings() -> Settings:
    """
    This function loads the configuration settings from the environment and returns them as a Settings object.

    Returns:
        Settings: A pydantic BaseSettings object containing the configuration settings.
    """
    log.info("Loading config settings from the environment...")
    return Settings()
