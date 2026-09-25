from app.chat.model import ChatEntries, MessageEntries, ReportRequest, ReportResponse
from app.chat.service import ChatService
from fastapi import APIRouter, HTTPException

router = APIRouter()
chat_service = ChatService()


@router.post("/v1/chat")
def create_new_chat(body: ChatEntries):
    return {"message": "created a new chat.", "data": body}


@router.post("/v1/message")
def add_new_message(body: MessageEntries):
    return {"message": "created a new message.", "data": body}


@router.post("/v1/report", response_model=ReportResponse)
def create_report(body: ReportRequest):
    try:
        return chat_service.create_report(question=body.question)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
