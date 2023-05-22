# FastAPI and Celery Integration Example

## Introduction
This repository provides a stripped-down demonstration of how to integrate FastAPI with Celery. To keep things straightforward and accessible, this example does not utilize Flower, differentiating it from other similar examples available on GitHub.

In this scenario, RabbitMQ serves as the message broker, while Redis functions as the result backend. We also illustrate how to incorporate async functions within Celery tasks.

(In `rpc-backend` branch, I also make an alternative in which rpc is used instead of redis for the result backend. Here is a brief comparison from the official celery documentation: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html)

## Setup and Installation
### Using Docker 
1. To host the project, start by building the Docker images for Celery and the API, using the commands below:

    ```
    # Build the Celery image
    docker build . -f worker.Dockerfile -t worker

    # Build the API image
    docker build . -f api.Dockerfile -t api 
    ```

2. Next, to spin up the Celery, FastAPI, RabbitMQ, and Redis containers together, use the following command:

    ```
    # Host the containers
    docker-compose up -d --build
    ```
   
3. After initializing the Docker containers, access the Swagger UI at http://localhost:8000/docs or interact with the API directly.

## How to Use
This API offers three main endpoints:

- `POST run_task`: Triggers a task that takes approximately 10 seconds to complete. Upon initiating this task, a unique task ID is generated for tracking progress and retrieving results.

- `GET status`: Allows users to track the status of a specific task using its ID.

- `GET result`: Retrieves the result of a completed task using its ID.

## Support
If you find this project useful, please consider giving the repository a star! 

For any queries or feedback, reach out to the author, Kenny Ng, at contact@kennyng.dev.
