# Copyright (C) 2021-2022 Archingen, PLC DBA PermitZIP.

"""
# Core Configuration

Set an environment variable named `USER_ENV` to `DEV` or `PROD`, or `LOCAL` to configure the environment.
This will initialize the package with the global variables required to perform various tasks.
The primary purpose is to generate the `CONFIG` object which is a dictionary of global variables.
Copyright 2022 Archingen, PLC.
"""

from typing import Dict
from pydantic import BaseSettings


class Settings(BaseSettings):
    # application and environment information
    user_env: str = None  # set to DEV, PROD, or LOCAL
    version: str = "0.0.1"
    library: str = "<<your-application-name"

    # clickup configs
    clickup_api_token: str = None
    clickup_api_base: str = None
    clickup_prod_workspace: str = None
    clickup_dev_workspace: str = None
    clickup_workspace: str = None

    # persistent layer
    mongo_uri_prod: str = None
    mongo_uri_dev: str = None
    mongo_uri_local: str = None
    mongo_uri: str = None
    database: str = None

    # email server credentials
    front_token_prod: str = None
    front_token_dev: str = None
    front_token_local: str = None
    front_token: str = None

    @property
    def environment_matcher(cls) -> Dict:
        """
        ## Match your environment!
        Uses the `user_env` variable to set the
        related environment variables stored in `.env` based on the
        environment.
            Args:
                settings (cls): The configured settings from core.config which read
                the `.env` file and prepare the settings class. See options above.
            Returns:
                settings (cls): the configured settings object
        """

        if cls.user_env == "DEV":
            cls.mongo_uri = cls.mongo_uri_dev
            cls.front_token = cls.front_token_dev
            cls.database = "DEV"
            cls.clickup_workspace = cls.clickup_dev_workspace
            print("Development environment configured!")

        elif cls.user_env == "PROD":
            cls.mongo_uri = cls.mongo_uri_prod
            cls.front_token = cls.front_token_prod
            cls.database = "GadgetBotIO"
            cls.clickup_workspace = cls.clickup_prod_workspace
            print("Production environment configured!")

        elif cls.user_env == "LOCAL":
            cls.mongo_uri = cls.mongo_uri_local
            cls.front_token = cls.front_token_dev
            cls.database = "LOCAL"
            cls.clickup_workspace = cls.clickup_dev_workspace
            print("Local environment configured!")

        else:
            raise Exception(
                "Was unable to determine the environment! Please set the USER_ENV environment variable. See documentation."
            )

        return cls

    class Config:
        env_file = ".env"


settings = Settings()


CONFIG: Dict = settings.environment_matcher
