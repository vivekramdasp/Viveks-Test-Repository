# Copyright (C) 2021-2022 Archingen, PLC DBA PermitZIP.

# Custom Dockerfile for Gadget Engineering contianer development. The base
# image is from microsoft and is compatible with VS Code Remote Containers plugin.
# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.231.6/containers/python-3/.devcontainer/base.Dockerfile

ARG VARIANT="3.9-bullseye"

# STAGES
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT} as base-image
# GLOBALS
ARG SOURCE_DIRECTORY="/workspaces/slack-triage-automation/src"
# The required location for runtime files for AWS Lambda is /var/runtime
ARG RUNTIME_DIRECTORY="/var/runtime/"
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster

FROM base-image as python-deps
# Copy source files to /var/runtime, the location where AWS Lambda looks to
# find runtime libraries
RUN mkdir ${RUNTIME_DIRECTORY}
COPY setup.py pyproject.toml Pipfile Pipfile.lock ${RUNTIME_DIRECTORY}
WORKDIR ${RUNTIME_DIRECTORY}
RUN pipenv install --deploy
RUN cp -r $(pipenv --venv)/lib/python3.9/site-packages/. ./

# Fresh base image
FROM base-image as runtime

# Pipenv installs the libraries in a sub directory. We must copy all of those libraries
# (site-packages) from the virtual environment into the runtime folder /var/runtime so AWS Lambda can find them.
COPY --from=python-deps ${RUNTIME_DIRECTORY} ${RUNTIME_DIRECTORY}

# Install the application src code into lambda runtime folder
WORKDIR ${RUNTIME_DIRECTORY}
COPY . .

# Run the application on port 8000
EXPOSE 8000
