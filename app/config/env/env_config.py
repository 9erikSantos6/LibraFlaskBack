import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import EnvConfigType


class EnvConfigurator:
    _env_config_name = None

    @staticmethod
    def get_env_name():
        if EnvConfigurator._env_config_name is None:
            env = os.getenv("FLASK_ENV", "development").upper()
            env = env.replace("-", "_").replace(" ", "_").replace(".", "_")

            if env not in EnvConfigType.__members__:
                raise ValueError(
                    f"Invalid environment name: {env}. "
                    f"Valid options are: {', '.join(EnvConfigType.__members__.keys())}"
                )
            EnvConfigurator._env_config_name = env
        return EnvConfigurator._env_config_name

    @staticmethod
    def load_app_config(app: Flask):
        env_name = EnvConfigurator.get_env_name()
        app.config.from_object(EnvConfigType[env_name].value)
