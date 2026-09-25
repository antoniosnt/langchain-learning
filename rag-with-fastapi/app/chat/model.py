from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class MessageEntries(BaseModel):
    content: str
    created_date: datetime
    updated_date: datetime


class ChatEntries(BaseModel):
    chat_title: str
    created_date: datetime
    updated_date: datetime


class ChatDTO(BaseModel):
    chat_id: int
    author_id: int
    chat_title: str
    created_date: datetime
    updated_date: datetime


class MessageDTO(BaseModel):
    content: str
    created_date: datetime
    updated_date: datetime


class ReportRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


class ReportResponse(BaseModel):
    message: str
    data: list[dict[str, Any]]
