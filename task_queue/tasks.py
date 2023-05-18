from celery import Celery
from asgiref.sync import async_to_sync
import asyncio

# app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://guest:guest@localhost:5672//')
app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')
app.set_default()
app.conf.update(task_track_started=True)
app.conf.update(task_serializer='pickle')
app.conf.update(result_serializer='pickle')
app.conf.update(accept_content=['pickle', 'json'])
app.conf.update(result_persistent=True)
app.conf.update(worker_send_task_events=False)
app.conf.update(worker_prefetch_multiplier=1)


async def wait_10_sec_and_return(input_dto):
    await asyncio.sleep(10)
    return input_dto['message']


@app.task
def wait_10_sec(input_dto):
    async_service_to_sync = async_to_sync(wait_10_sec_and_return)
    return async_service_to_sync(input_dto)

@app.task
def add(x,y):
    return x + y