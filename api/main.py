from typing import Union
from task_queue import tasks
from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel
from task_queue.tasks import wait_10_sec

app = FastAPI()


class InputDto(BaseModel):
    message: str = ''


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/run_task")
def run_task(input_dto: InputDto):
    json_body = input_dto.dict()
    result = wait_10_sec.delay(json_body)
    return {'task_id': result.id}


@app.get("/task_status")
def get_task_status(task_id):
    task_result = AsyncResult(id=task_id)
    res = {
        "id": task_id,
        "status": task_result.ready()
    }
    return res


@app.get("/tasK_result")
def get_result(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "id": task_id,
        "task_result": task_result.result
    }
    return result
