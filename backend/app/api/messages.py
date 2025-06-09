from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate, Message as MessageSchema, Conversation
from app.api.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=MessageSchema)
async def create_message(
    message: MessageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_message = Message(
        sender_id=current_user.id,
        receiver_id=message.receiver_id,
        property_id=message.property_id,
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@router.get("/conversations", response_model=List[Conversation])
async def get_conversations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Get all unique conversations for the current user
    conversations = db.query(Message).filter(
        (Message.sender_id == current_user.id) | 
        (Message.receiver_id == current_user.id)
    ).order_by(Message.created_at.desc()).all()
    
    # Process conversations to get the latest message for each user
    conversation_map = {}
    for msg in conversations:
        other_user_id = msg.receiver_id if msg.sender_id == current_user.id else msg.sender_id
        if other_user_id not in conversation_map:
            other_user = db.query(User).filter(User.id == other_user_id).first()
            conversation_map[other_user_id] = {
                "user_id": other_user_id,
                "user_name": other_user.full_name,
                "last_message": msg.content,
                "last_message_time": msg.created_at,
                "unread_count": 0,
                "property_id": msg.property_id,
                "property_title": msg.property.title
            }
    
    return list(conversation_map.values())

@router.get("/{property_id}/{user_id}", response_model=List[MessageSchema])
async def get_messages(
    property_id: int,
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    messages = db.query(Message).filter(
        ((Message.sender_id == current_user.id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == current_user.id)),
        Message.property_id == property_id
    ).order_by(Message.created_at.asc()).all()
    
    # Mark messages as read
    for msg in messages:
        if msg.receiver_id == current_user.id and not msg.is_read:
            msg.is_read = True
    db.commit()
    
    return messages 