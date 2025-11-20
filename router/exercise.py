from datetime import datetime
from fastapi import APIRouter

from db import create_exercise
from db.models import RequestExercise, ResponseExercise

router = APIRouter()


@router.get("/exercise")
async def get_exercises():
    return {"message": "Get Exercises Triggered"}


@router.get("/exercise/{id}")
async def get_exercise(id: int):
    return {"message": f"Get Exercise {id} Triggered"}


@router.post("/exercise")
async def add_exercise(exercise: RequestExercise) -> ResponseExercise:

    # Get timestamp
    created_at = datetime.now()

    # Create full Exercise data model
    response_exercise: ResponseExercise = ResponseExercise(
        name=exercise.name,
        muscle_group=exercise.muscle_group,
        category=exercise.category,
        created_at=created_at,
    )

    # Save Exercise data to db
    await create_exercise(new_exercise=response_exercise)

    return response_exercise


@router.put("/exercise/{id}")
async def update_exercise(id: int):
    return {"message": f"Update Exercise {id} Triggered"}


@router.delete("/exercise/{id}")
async def delete_exercise(id: int):
    return {"message": f"Delete Exercise {id} Triggered"}
