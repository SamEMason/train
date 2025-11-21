import sqlite3
from datetime import datetime

from db.queries import (
    ADD_EXERCISE,
    CREATE_EXERCISE_TABLE,
    SELECT_ALL_EXERCISES,
    SELECT_EXERCISE_BY_ID,
)
from db.models import ExerciseRequestBody

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
