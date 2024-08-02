# FastAPI LLM

This project is a FastAPI application designed to connect to AWS Bedrock and Sagemaker LLMs.

## Setup

1. Install Poetry: https://python-poetry.org/docs/#installation
```sh
# Setup Virtual Environment
make setup
```

## Running the app
```sh
# run locally in the virtual environment
make run-local

# Run with docker-compose
make run-docker
```

## Linting, Formatting and Type Checking
```sh
make lint
```

## Testing
```sh
make test
```

## Cleaning up the Repo and Docker
```sh
make clean
```

## Deployment
GitHub Actions are defined in .github/workflows/build-and-push.yml and enable the following components to fully and continuously deploy application code:
1. verify linting, formatting
2. Execute unit testing
3. build a docker container and push to AWS ECR
4. Deploy the new container into ECS Fargate infrastructure by applying the new container image to the llm-infra terraform repository

The terraform state file is shared on my terraform account:
https://app.terraform.io/app/ScottCronin/workspaces/scottcronin

Please see [llm-infra code](https://github.com/jscottcronin/llm-infra) for the managed infrastructure which includes the following resources:
* VPC
* ALB
* ECS[Fargate]
* ECR
* AWS Bedrock IAM Roles

