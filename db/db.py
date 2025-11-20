import sqlite3

from db.queries import CREATE_EXERCISE_TABLE

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_EXERCISE_TABLE)
