import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import ConfigType

class EnvConfigurator:
    ENV_CONFIG_NAME = os.getenv("FLASK_ENV", "default").upper()
    @staticmethod
    def configure_env(app: Flask):
        if EnvConfigurator.ENV_CONFIG_NAME not in ConfigType.__members__:
            raise ValueError(f"Invalid environment name: {EnvConfigurator.ENV_CONFIG_NAME}")
        app.config.from_object(ConfigType[EnvConfigurator.ENV_CONFIG_NAME].value)
        
    @staticmethod
    def configure_database(db: SQLAlchemy):
        if EnvConfigurator.ENV_CONFIG_NAME != ConfigType.PRODUCTION.name:
            db.create_all()