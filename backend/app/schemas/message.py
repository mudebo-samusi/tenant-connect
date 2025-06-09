from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageBase(BaseModel):
    content: str
    property_id: int
    receiver_id: int

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    sender_id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Conversation(BaseModel):
    user_id: int
    user_name: str
    last_message: str
    last_message_time: datetime
    unread_count: int
    property_id: int
    property_title: str 