CREATE_EXERCISE_TABLE = """CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    name TEXT,
    muscle_group TEXT,
    category TEXT,
    created_at TIMESTAMP
);"""


ADD_EXERCISE = """INSERT INTO exercises (name, muscle_group, category, created_at) VALUES (?, ?, ?, ?);"""

SELECT_ALL_EXERCISES = "SELECT * FROM exercises;"

SELECT_EXERCISE_BY_ID = """SELECT * FROM exercises
WHERE id = ?"""

DELETE_EXERCISE = "DELETE FROM exercises WHERE id = ?"
