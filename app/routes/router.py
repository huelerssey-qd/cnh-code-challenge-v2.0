from fastapi import APIRouter

from app.routes.challenge.route import router as challenge_router

api_router = APIRouter()

api_router.include_router(challenge_router, prefix="/api/v1", tags=["Challenge"])
