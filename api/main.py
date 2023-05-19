from typing import Union
from worker import tasks
from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel
from worker.tasks import example_task

app = FastAPI()


class ExampleInputModel(BaseModel):
    message: str = ''


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/example_task")
def run_task(input_dto: ExampleInputModel):
    json_body = input_dto.dict()
    result = example_task.delay(json_body)
    return {'task_id': result.id}


@app.get("/status")
def get_task_status(task_id):
    task_result = AsyncResult(id=task_id)
    res = {
        "id": task_id,
        "status": task_result.ready()
    }
    return res


@app.get("/result")
def get_result(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "id": task_id,
        "task_result": task_result.get()
    }
    return result
