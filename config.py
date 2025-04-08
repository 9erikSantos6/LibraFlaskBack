import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, "app/db")
os.makedirs(DB_DIR, exist_ok=True)


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DB_DIR, "LibraFlask.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
