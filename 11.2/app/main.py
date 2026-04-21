from itertools import count
from threading import Lock

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(title="Task 11.2")

memory_db: dict[int, dict] = {}
_id_seq = count(start=1)
_id_lock = Lock()


def reset_memory_state() -> None:
    global _id_seq
    with _id_lock:
        memory_db.clear()
        _id_seq = count(start=1)


def next_user_id() -> int:
    with _id_lock:
        return next(_id_seq)


class UserIn(BaseModel):
    username: str
    age: int


class UserOut(UserIn):
    id: int


@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: UserIn) -> dict:
    user_id = next_user_id()
    memory_db[user_id] = user.model_dump()
    return {"id": user_id, **memory_db[user_id]}


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int) -> dict:
    if user_id not in memory_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **memory_db[user_id]}


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int) -> Response:
    if memory_db.pop(user_id, None) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=204)
