# [ADD PROJECT NAME]

Copyright (C) 2021 Archingen, PLC DBA PermitZIP.

This project is configured as a Python project with container-based development
as a project to deploy to an Amazon Lambda function.

Note: you will have to add your own .env file to the root in order to ensure the core configuration works for your project.

---

## Administrative Information

### ๐ Important Folders and Files

#### ๐ ๐ง .devcontainer

The Dockerfile and .dockerignore files for building the development containers.

Creating containers (VS Code) with the following quick steps:

1. Install Docker (if using Windows, you will need WSL to run Docker).
2. Install the Remote-Containers plugin for **VS Code**
3. Clone the repository and select the `reopen in container` option. VS Code
   will build the container and open a session of the repository within the
   container.

#### ๐ ๐พ src

The primary code base for the application.

##### ๐ ๐ฅ cli

A place to build your own command line interface tools if applicable. If you delete, be sure to remove also the `click` dependenceis that come pre-packaged with this setup.

##### ๐ ๐ core

Core configuration for environment management.

##### ๐ ๐ซฅ models

Class and data models.

#### ๐ ๐งช tests

Testing scripts, intentionally not included in the `src` folder to keep the
build package size slim.

#### ๐ ๐ณ Root Director Files

- ๐ `.dockerignore` is setup to exclude everything but what is explicitly listed.

- ๐ `.gitignore` has been preconfigured to cover most required gitignore
  conditions. Update as required based on your project needs.

- ๐ `Dockerfile` is the image build instruction for Production.

- ๐ `Pipfile` the pipefil which includes some baseline requirements useful for most
  packages. You can get started in development quickly by running `pipenv install --dev`. This will create the virtual environment and install all dependencies (including the
  dev dependencies).

- ๐ `Pipefile.lock` Pipenv manages this for you.

- ๐ `pipenv` Pipenv manages this for you (for the most part)

- ๐ `README.md` is this document. Delete this information and update with your own information as you develop.

- ๐ `setup.py` is used for the build. Don't worry about this unless you plan to
  issue to PyPy.

- ๐ `pyproject.toml` is part of the build instruction for Python. Don't modify
  unless you know what you're doing.
