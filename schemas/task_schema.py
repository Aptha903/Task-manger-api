from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.task import StatusEnum

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[StatusEnum] = StatusEnum.pending
    due_date: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    due_date: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: StatusEnum
    due_date: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
