import os

from flask import Flask
from config import EnvConfigType


class EnvConfigurator:
    _env_config_name = None
    _create_default_admin = None

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

    @staticmethod
    def criar_admin_padrao_definido():
        if EnvConfigurator._create_default_admin is None:
            value = os.getenv("SERVER_CREATE_DEFAULT_ADMIN", "false").strip().lower()
            EnvConfigurator._create_default_admin = value in ["true", "1", "yes"]
        return EnvConfigurator._create_default_admin

    @staticmethod
    def get_config():
        env_name = EnvConfigurator.get_env_name()
        config_class = EnvConfigType[env_name].value
        return config_class