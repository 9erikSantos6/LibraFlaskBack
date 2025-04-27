from flask import Flask
from config import EnvConfigType

from flask_sqlalchemy import SQLAlchemy
from app.config.env.env_config import EnvConfigurator


class DatabaseConfigurator:
    @staticmethod
    def init_db(app: Flask, db: SQLAlchemy):
        from app import models

        if EnvConfigurator.get_env_name() != EnvConfigType.PRODUCTION.name:
            db.create_all()
