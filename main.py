from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Sj(BaseModel):
    id: int
    name: str
    origin: str

sjs: List[Sj] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FASTAPI"}


@app.get("/sjs")
def get_sjs():
    return sjs



@app.post("/sjs")
def add_sj(sj: Sj):
    sjs.append(sj)
    return sj



@app.put("/sjs/{sj_id}")
def update_sj(sj_id: int, updated_sj: Sj):
    for index, sj in enumerate(sjs):
        if sj.id == sj_id:
            sjs[index] = updated_sj
            return updated_sj
    return {"error": "Sj not found"}



@app.delete("/sjs/{sj_id}")
def delete_sj(sj_id: int):
    for index, sj in enumerate(sjs):
        if sj.id == sj_id:
            deleted = sjs.pop(index)
            return deleted
    return {"error": "Sj not found"}
