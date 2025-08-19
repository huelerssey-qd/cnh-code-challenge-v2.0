from enum import Enum
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Environment(str, Enum):
    DEV = "dev"
    HOMOLOG = "homolog"
    PROD = "prod"


class AppEnvironmentSettings(BaseSettings):
    environment: Environment = Environment.DEV

    model_config = {
        "env_prefix": "APP_",
        "extra": "forbid",
    }


class OpenAISettings(BaseSettings):
    api_key: str
    model_name: str = "gpt-4o"

    model_config = {
        "env_prefix": "OPENAI_",
        "extra": "forbid",
    }


class SentrySettings(BaseSettings):
    dns: str

    model_config = {
        "env_prefix": "SENTRY_",
        "extra": "forbid",
    }


class SecuritySettings(BaseSettings):
    secret_key: str

    model_config = {
        "env_prefix": "SECURITY_",
        "extra": "forbid",
    }


class Settings(BaseSettings):
    sentry: SentrySettings = SentrySettings()
    openai: OpenAISettings = OpenAISettings()
    security: SecuritySettings = SecuritySettings()
    env: AppEnvironmentSettings = AppEnvironmentSettings()

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
        "extra": "allow",
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
