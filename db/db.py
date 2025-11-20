import sqlite3

from db.queries import ADD_EXERCISE, CREATE_EXERCISE_TABLE
from db.models import ResponseExercise

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_EXERCISE_TABLE)


async def create_exercise(new_exercise: ResponseExercise) -> None:
    with connection:
        connection.execute(
            ADD_EXERCISE,
            (
                new_exercise.name,
                new_exercise.muscle_group,
                new_exercise.category,
                new_exercise.created_at,
            ),
        )
