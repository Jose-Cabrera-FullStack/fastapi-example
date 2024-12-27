# Payment Service


## Description
`payment-service` is a Python-based API project built using FastAPI, a high-performance web framework for creating RESTful APIs.

This project provides a solid foundation and structure to develop scalable and maintainable APIs.

The service is specifically designed for the integration between Paracas and **ASBANC/BCP** to manage and process client debts and payments. It implements key principles of **Clean Architecture**, **Hexagonal architecture**, **SOLID principles**, and **Onion architecture** to ensure a robust and flexible design.

The service handles critical operations like debt validation, status checks, payment processing, and payment reversal, aimed at enhancing operational efficiency and security in the financial interactions of the Paracas system.

## Endpoints

The service provides the following endpoints:

```python
/: Return the Swagger UI documentation.
/v1/debt-status: Return the status of a debt.
/v1/update-debt-payment: Update the payment status of a debt.
/v1/revert-debt-payment: Revert the payment status of a debt.
```


## Installation

```
python3 -m venv venv
source venv/bin/activate
# source venv/Scripts/activate - Windows
pip install -r requirements.txt
```

## Environment Variables

The project uses environment variables to configure the application. The environment variables are loaded from a `.env` file located in the root directory of the project. Use the `.env.example` file as a template to create your own `.env` file.

```bash
# .env
DATABASE_URL=postgresql://paracas:paracas@db:5432/payment_service
...
```

## Docker: Run Project

### Run build container

```bash
docker build -f docker/Dockerfile.dev -t payment-service .
```

### Run  the container

```bash
docker-compose -f docker/docker-compose.yml up --force-recreate --build

# check sql container
docker-compose -f docker/docker-compose.yml exec db psql --username=postgres --dbname=payment # env variables
```

With the **docker-compose** configuration, this generate a API endpoint in the port 8000. You can access to the API in the following URL: http://localhost:8000

### Migrations

The project uses Alembic to manage database migrations. Alembic is a lightweight database migration tool for SQLAlchemy.

```bash
Terminal 1:
docker-compose -f docker/docker-compose.yml up

Terminal 2:
docker-compose -f docker/docker-compose.yml exec app bash

#Apply migration
alembic upgrade head

# Note: To create a migration runs this command
#Generate migration
alembic revision --autogenerate -m "migration message"

```
***Note**: If it is the first migration, you have to excecute every migration sequentialy*

```bash
Example:

docker-compose -f docker/docker-compose.yml exec app bash
alembic upgrade b1b4b618e741
alembic upgrade populate_fake_data
```
***Note**: If you only want to run the migrations, you can use the following command*

```bash
docker-compose -f docker/docker-compose.yml exec app alembic upgrade head
```

The project uses a PostgreSQL database. You can access the database using the following command:

```bash
docker-compose -f docker/docker-compose.yml exec db psql --username=paracas --dbname=payment_service
```

### Access PgAdmin

Pre-requisitos:
- The PgAdmin service must be configured in the docker-compose file

Open your web browser and navigate to:
- http://localhost:5050

Use the configured credentials to log in:
- User: `admin@admin.com`
- Pass: `admin`

Create a new connection:
- Server name/address: `db` (Service name in docker-compose file)
- Port: 5432
- Database name: `payment_service`
- Enter database connection credentials

### Run tests

```bash
Terminal 1:
docker-compose -f docker/docker-compose.yml up

Terminal 2:
docker-compose -f docker/docker-compose.yml exec app bash
python -m pytest --cov=app --cov-report=term --cov-config=.coveragerc
```

## Project Structure
```bash
fast-api-base
├─ .gitignore
├─ app
│  ├─ adapter
│  │  ├─ async_tasks.py
│  │  └─ __init__.py
│  ├─ database
│  │  └─ __init__.py
│  ├─ domain
│  │  └─ __init__.py
│  ├─ infrastructure
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ schemas
│  │  ├─ request.py
│  │  └─ response.py
│  ├─ service
│  │  └─ __init__.py
│  ├─ settings.py
│  ├─ tests
│  │  ├─ test_app.py
│  │  └─ __init__.py
│  └─ utils
│     ├─ custom_http_response.py
│     └─ tools.py
├─ scripts
│  └─ extract_openapi.py
├─ docker
│  └─ docker-compose.yml
│  └─ Dockerfile.dev
│  └─ Dockerfile.prod
│  └─ .dockerignore
├─ pytest.ini
├─ README.md
├─ requirements.txt
├─ start-container.sh
└─ supervisord.conf
```

## Scaffolding and Architecture

The project follows a well-organized directory structure:

**app**: This directory contains the main app-related code.

**adapter**: Contains files that connect the service with external services from infrastructure.

**database**: Directory that potentially holds code related to database configuration, connections and models.

**domain**: Contains files representing the project's domain logic.

**infrastructure**: Contains files managing the technical infrastructure of the application.

**main.py**: The main app file where the FastApi application is defined and configured.

**schemas**: Contains data schemas used for app incoming requests and outgoing responses.

**service**: Contains files connect the domain with particular uses cases for the app.

**settings.py**: File to store app configuration, such as environment variables, etc.

**tests**: Directory for automated app tests.

**utils**: Contains utility functions or common tools used in the application.

**scripts**: Contains scripts to help with the development process.

**Note**: These articles is based on the following: 

- [Hexagonal Architecture](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63).
- [FastAPI with Ormar, Docker and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/).

**References**: Inspired by [refactoring](https://refactoring.guru/es/design-patterns/), [12factor](https://12factor.net/es/)

