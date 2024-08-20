from fastapi import APIRouter

from .endpoints import ai_function

router = APIRouter()
router.include_router(ai_function.router, prefix="/ai", tags=["AI"])
