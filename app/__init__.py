from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app import models

        db.create_all()  # cria as tabelas

        from .routers import main_bp, livro_bp
        from .routers import main_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(livro_bp)
        pass

    return app
