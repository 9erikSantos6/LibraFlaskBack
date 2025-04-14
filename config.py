import os
from dotenv import load_dotenv
from enum import Enum


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))

DB_DIR = os.path.join(BASE_DIR, "app/db")
os.makedirs(DB_DIR, exist_ok=True)


def validade_server_port(port):
        try:
            port = int(port)
        except ValueError:
            raise ValueError("SERVER_PORT precisa ser um número inteiro")
        if port < 1024 or port > 65535:
            raise ValueError("SERVER_PORT must be between 1024 and 65535")
        return port

class Config:
    SERVER_PORT = validade_server_port(os.getenv("SERVER_PORT", 15000))
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{os.path.join(BASE_DIR, 'app/db/LibraFlask.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ConfigType(Enum):
    DEVELOPMENT = DevelopmentConfig
    PRODUCTION = ProductionConfig
    TESTING = TestingConfig
    DEFAULT = Config