from fastapi import FastAPI

from db import create_tables
from router.exercise import router as exercise_router

create_tables()

app = FastAPI()


app.include_router(exercise_router)
