from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class TaskBase(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the task")
    description: str = Field(..., min_length=1, description="The description of the task")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    is_completed: bool = False