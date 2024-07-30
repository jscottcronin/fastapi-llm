# FastAPI LLM

This project is a FastAPI application designed to connect to AWS Bedrock and Sagemaker LLMs.

## Setup

1. Install Poetry: https://python-poetry.org/docs/#installation
2. Install dependencies: `poetry install`
3. Install pre-commit hooks: `poetry run pre-commit install`

## Running the app locally

```bash
poetry run uvicorn app.main:app --reload
```