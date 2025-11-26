import sqlite3
from datetime import datetime

from db.queries import (
    ADD_EXERCISE,
    CREATE_EXERCISE_TABLE,
    DELETE_EXERCISE,
    SELECT_ALL_EXERCISES,
    SELECT_EXERCISE_BY_ID,
)
from db.models import ExerciseCreate, ExerciseUpdate

connection = sqlite3.connect("data.db")


def create_tables():
    # Execute create exercise query
    with connection:
        connection.execute(CREATE_EXERCISE_TABLE)


async def create_exercise(
    new_exercise: ExerciseCreate, created_at: datetime
) -> int | None:
    # Execute add exercise query
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

    # Return created exercise row id
    return cursor.lastrowid


async def get_all_exercises():
    # Execute select exercise query
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_EXERCISES)

        # Return exercise rows
        return cursor.fetchall()


async def get_exercise_by_id(id: int):
    # Execute select exercise query with id argument
    with connection:
        cursor = connection.execute(SELECT_EXERCISE_BY_ID, (id,))

        # Return exercise row
        return cursor.fetchone()


async def modify_exercise(id: int, payload: ExerciseUpdate):
    fields: list[str] = []
    values: list[str] = []

    # Extract data from payload
    data = payload.model_dump(exclude_unset=True)

    # Dynamically create string of fields to update
    # Add values to list to use as tuple argument with query
    for key, value in data.items():
        fields.append(f"{key} = ?")
        values.append(value)

    # Return if there are no values to update
    if len(values) == 0:
        return

    # Build query for execution
    query = f"UPDATE exercises SET {", ".join(fields)} WHERE id = {id}"

    # Execute update exercise query
    with connection:
        connection.execute(query, tuple(values))


async def delete_exercise(id: int):
    # Execute delete exercise query
    with connection:
        connection.execute(DELETE_EXERCISE, (id,))
