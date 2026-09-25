from app.chat.model import ChatEntries, MessageEntries
from fastapi import APIRouter

router = APIRouter()


@router.post("/v1/chat")
def create_new_chat(body: ChatEntries):
    return {"message": "created a new chat.", "data": body}


@router.post("/v1/message")
def add_new_message(body: MessageEntries):
    return {"message": "created a new message.", "data": body}
