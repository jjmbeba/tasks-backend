from pydantic import BaseModel, ConfigDict

class Task(BaseModel):
    id: int
    name: str
    description: str