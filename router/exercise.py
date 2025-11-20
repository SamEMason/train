from fastapi import APIRouter

router = APIRouter()


@router.get("/exercise")
def get_exercises():
    return {"message": "Get Excercises Triggered"}


@router.get("/exercise/{id}")
def get_exercise(id: int):
    return {"message": f"Get Excercise {id} Triggered"}


@router.post("/exercise")
def add_exercise():
    return {"message": "Add Excercise Triggered"}


@router.put("/exercise/{id}")
def update_exercise(id: int):
    return {"message": f"Update Excercise {id} Triggered"}


@router.delete("/exercise/{id}")
def delete_exercise(id: int):
    return {"message": f"Delete Excercise {id} Triggered"}
