from typing import List

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the backend."""

    API_PREFIX: str
    DEBUG: bool
    ALLOWED_ORIGINS: str
    MISTRAL_MODEL: str
    MISTRAL_API_KEY: str
    DATABASE_URL: str
    UPLOADTHING_TOKEN: str
    CLERK_SECRET_KEY: str
    CLERK_JWT_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def split_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
