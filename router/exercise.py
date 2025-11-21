from datetime import datetime
from fastapi import APIRouter, HTTPException

from db import create_exercise, delete_exercise, get_all_exercises, get_exercise_by_id
from db.models import ExerciseRequestBody, ExerciseResponseBody

router = APIRouter()


@router.get("/exercise", status_code=200)
async def get_exercises() -> list[ExerciseResponseBody]:
    rows = await get_all_exercises()

    return [
        ExerciseResponseBody(
            id=row[0],
            name=row[1],
            muscle_group=row[2],
            category=row[3],
            created_at=row[4],
        )
        for row in rows
    ]


@router.get("/exercise/{id}", status_code=200)
async def get_exercise(id: int) -> ExerciseResponseBody:
    row = await get_exercise_by_id(id)

    if row is None:
        # Row not found - return 404
        raise HTTPException(status_code=404, detail="Exercise not found")

    return ExerciseResponseBody(
        id=row[0],
        name=row[1],
        muscle_group=row[2],
        category=row[3],
        created_at=row[4],
    )


@router.post("/exercise", status_code=201)
async def add_exercise(exercise: ExerciseRequestBody) -> ExerciseResponseBody:

    # Get timestamp
    created_at = datetime.now()

    # Save Exercise data to db
    new_id = await create_exercise(new_exercise=exercise, created_at=created_at)

    if new_id is None:
        raise HTTPException(
            status_code=500, detail="Failed to create exercise in the database"
        )

    # Create full Exercise data model
    response_exercise = ExerciseResponseBody(
        id=new_id,
        name=exercise.name,
        muscle_group=exercise.muscle_group,
        category=exercise.category,
        created_at=created_at,
    )

    return response_exercise


@router.put("/exercise/{id}", status_code=200)
async def update_exercise(id: int):
    return {"message": f"Update Exercise {id} Triggered"}


@router.delete("/exercise/{id}", status_code=204)
async def remove_exercise(id: int):
    row = await get_exercise_by_id(id)

    if row is None:
        raise HTTPException(status_code=404, detail="Exercise not found")

    await delete_exercise(id)
    return None
