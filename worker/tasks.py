from celery import Celery
from asgiref.sync import async_to_sync
import asyncio

# Initializing celery app
app = Celery('tasks', backend='redis://redis:6379', broker='pyamqp://rabbitmq:5672')
app.set_default()
app.conf.update(task_track_started=True)
app.conf.update(result_persistent=True)
app.conf.update(worker_send_task_events=False)


# A dummy async function which emulates the behavior of computations
async def wait_10_sec_and_return(user_input):
    await asyncio.sleep(10)
    return user_input['message']


@app.task
def example_task(user_input):
    # Turning async function into a sync one, as async functions are not supported in celery
    async_service_to_sync = async_to_sync(wait_10_sec_and_return)
    return async_service_to_sync(user_input)

