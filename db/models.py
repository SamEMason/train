from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ExerciseRequestBody(BaseModel):
    name: str
    muscle_group: str
    category: str


class ExerciseResponseBody(BaseModel):
    id: int
    name: str
    muscle_group: str
    category: str
    created_at: datetime


class ExerciseUpdate(BaseModel):
    name: Optional[str] = None
    muscle_group: Optional[str] = None
    category: Optional[str] = None
