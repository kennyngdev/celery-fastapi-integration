# FastAPI Celery Integration Example

## Forword
I created this repository to show a barebone implementation of integrating FastAPI with Celery. 
Unlike other repositories on GitHub demonstrating the same possibility, 
flower is not used in this one as I wanted to make it as simple as it can be.

In this example, rabbitmq is used as the message broker and redis is used as the result backend.

Also, I added an example on how async function can be used on celery.

## Project Setup
### Docker Build
You can host the project by running the following commands:
```
# build image for celery
docker build . -f worker.Dockerfile -t worker
# build image for api
docker build . -f api.Dockerfile -t api 
# host celery, fastapi, rabbitmq and redis containers together
docker-compose up -d --build
```
After hosting the containers on Docker, you can go to http://localhost:8000/docs to go the swagger UI or just call the API directly.

## Usage
By trigger the `POST run_task` endpoint, a task which takes 10 second will be trigger. A task ID will be issued for tracking progress and getting result.

`GET status` can be used to track the status of a task with its ID.

`GET result` can be used to get the result of the task.

## Contact
Please give the repo a star if you like it!
This app is written by Kenny Ng (contact@kennyng.dev).