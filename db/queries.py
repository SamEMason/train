CREATE_EXERCISE_TABLE = """CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    name TEXT,
    muscle_group TEXT,
    category TEXT,
    created_at TIMESTAMP
);"""


ADD_EXERCISE = """INSERT INTO exercises (name, muscle_group, category, created_at) VALUES (?, ?, ?, ?)"""