from fastapi import FastAPI

from app.routes.router import api_router
from app.settings.app_config import AppConfig


config = AppConfig()

app = FastAPI(
    title="Code Challenge API",
    description="API for the team code challenge. Implements mathematical operations via the /challenge route.",
    version="1.0.0",
    openapi_url=f"{config.get_root_path()}/openapi.json",
    root_path=config.get_root_path(),
)

app.include_router(api_router)
