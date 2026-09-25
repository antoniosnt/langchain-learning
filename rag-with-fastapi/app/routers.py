from app.chat.routes import router as chatbot_router
from fastapi import APIRouter

router = APIRouter(prefix="/api")

router.include_router(router=chatbot_router)
