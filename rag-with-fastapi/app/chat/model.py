from datetime import datetime

from pydantic import BaseModel


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
