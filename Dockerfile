# Copyright (C) 2021-2022 Archingen, PLC DBA PermitZIP.

# install AWS python3.9
FROM amazon/aws-lambda-python:3.9 AS base

FROM base AS python-deps

RUN pip install pipenv
COPY setup.py pyproject.toml Pipfile Pipfile.lock .env ${LAMBDA_RUNTIME_DIR}
WORKDIR ${LAMBDA_RUNTIME_DIR}

# After install, move site-packages to app root to work with AWS lambda
RUN pipenv install --deploy && cp -r $(pipenv --venv)/lib/python3.9/site-packages/. ./

FROM python-deps AS runtime
# Required to create user account in later steps.
# RUN yes | yum install shadow-utils

# Create and switch to a new user
# RUN useradd --create-home appuser
# WORKDIR /home/appuser
# USER appuser
WORKDIR ${LAMBDA_RUNTIME_DIR}
# Install application into container
COPY . .

# Run the application on port 8000
EXPOSE 8000

CMD ["src.main.handler"]