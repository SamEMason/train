from datetime import datetime
from pydantic import BaseModel


class RequestExercise(BaseModel):
    name: str
    muscle_group: str
    category: str


class ResponseExercise(BaseModel):
    name: str
    muscle_group: str
    category: str
    created_at: datetime
