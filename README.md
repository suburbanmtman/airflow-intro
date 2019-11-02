# airflow-intro
Introduction to **[Apache Airflow](https://airflow.apache.org/)**, demonstrating how to get started quickly and be ready for higher scale production environments
using docker container orchestration.

## Prerequisites

**[Docker Desktop](https://www.docker.com/products/docker-desktop)**

**[Docker Compose](https://docs.docker.com/compose/install/)**

## Starting/Stopping
To start navigate to the version of the architecture you'd like to run (e.g. `versions/simple`) and run:

`docker-compose up -d --build`

To stop the environment run:

`docker-compose down`

## Architectures
### [Simple](versions/simple)

The simplest Airflow architecture where the webserver and scheduler run on a single container using the Sequential Executor.
A SQLite database is used for storing dag, task, xcom information, etc.

Local port forwarding:

|Local Port|Service|
|----------|-------|
|8080      |Airflow Webserver|

### [Celery](versions/celery)

A distributed Airflow architecture where the webserver and scheduler run on separate containers with one or more worker containers using the Celery Executor.
The components share a PostgreSQL database for dag, task, xcom informatin and communicate via Celery using Redis as a broker and PostgreSQL for a backend.

Local port forwarding:

|Local Port|Service|
|----------|-------|
|5433      | Airflow PostgreSQL DB|
|5555      | Airflow Flower Web UI|
|6379      | Redis Celery Broker|
|8080      | Airflow Webserver|

## Code Development

Since each version uses Docker Compose volumes to map the local python modules to the airflow webserver, scheduler, and workers,
any changes made to the [example](src/example) module will be reflect immediately in all of those containers.
