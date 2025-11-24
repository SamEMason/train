import sqlite3
from datetime import datetime
from typing import Any

from db.queries import (
    ADD_EXERCISE,
    CREATE_EXERCISE_TABLE,
    DELETE_EXERCISE,
    SELECT_ALL_EXERCISES,
    SELECT_EXERCISE_BY_ID,
)
from db.models import ExerciseRequestBody, ExerciseUpdate

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_EXERCISE_TABLE)


async def create_exercise(
    new_exercise: ExerciseRequestBody, created_at: datetime
) -> int | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            ADD_EXERCISE,
            (
                new_exercise.name,
                new_exercise.muscle_group,
                new_exercise.category,
                created_at,
            ),
        )

    return cursor.lastrowid


async def get_all_exercises():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_EXERCISES)

        return cursor.fetchall()


async def get_exercise_by_id(id: int):
    with connection:
        cursor = connection.execute(SELECT_EXERCISE_BY_ID, (id,))

        return cursor.fetchone()


async def modify_exercise(id: int, payload: ExerciseUpdate):
    fields: list[str] = []
    values: list[Any] = []

    data = payload.model_dump(exclude_unset=True)

    for key, value in data.items():
        fields.append(f"{key} = ?")
        values.append(value)

    if len(values) == 0:
        return

    query = f"UPDATE exercises SET {", ".join(fields)} WHERE id = {id}"

    with connection:
        connection.execute(query, tuple(values))


async def delete_exercise(id: int):
    with connection:
        connection.execute(DELETE_EXERCISE, (id,))
