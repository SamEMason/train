from datetime import datetime
from pydantic import BaseModel


class ExerciseRequestBody(BaseModel):
    name: str
    muscle_group: str
    category: str


class ExerciseResponseBody(BaseModel):
    name: str
    muscle_group: str
    category: str
    created_at: datetime
