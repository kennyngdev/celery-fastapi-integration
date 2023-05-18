# celery-fastapi-integration

## Project Setup
1. Run `pip install -r requirements` to install required libraries
2. Run `docker run -d -p 5672:5672 rabbitmq` to run rabbitmq on docker, in which we will use it as the message broker
3. Run `docker run -d -p 6379:6379 redis` to start redis, in which we use as the result backend for celery
3. Run `celery -A tasks worker --loglevel=INFO` to start celery
4. Run `uvicorn api.main:app --reload` to start FastAPI