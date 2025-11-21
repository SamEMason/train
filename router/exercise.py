from datetime import datetime
from fastapi import APIRouter

from db import create_exercise, get_all_exercises, get_exercise_by_id
from db.models import ExerciseRequestBody, ExerciseResponseBody

router = APIRouter()


@router.get("/exercise")
async def get_exercises() -> list[ExerciseResponseBody]:
    rows = await get_all_exercises()

    return [
        ExerciseResponseBody(
            name=row[1],
            muscle_group=row[2],
            category=row[3],
            created_at=row[4],
        )
        for row in rows
    ]


@router.get("/exercise/{id}")
async def get_exercise(id: int) -> ExerciseResponseBody:
    row = await get_exercise_by_id(id)

    return ExerciseResponseBody(
        name=row[1],
        muscle_group=row[2],
        category=row[3],
        created_at=row[4],
    )


@router.post("/exercise")
async def add_exercise(exercise: ExerciseRequestBody) -> ExerciseResponseBody:

    # Get timestamp
    created_at = datetime.now()

    # Create full Exercise data model
    response_exercise: ExerciseResponseBody = ExerciseResponseBody(
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
