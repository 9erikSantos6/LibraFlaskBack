from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

from app.config import BlueprintCreator, EnvConfigurator


db = SQLAlchemy()

APP_BLUEPRINTS = [
    # (module_name, blueprint_name)
    ("app.routers.main_router", "main_bp"),
    ("app.routers.livro_router", "livro_bp"),
]


def create_app():
    app = Flask(__name__)

    EnvConfigurator.configure_env(app)

    db.init_app(app)

    with app.app_context():
        from app.models.livro import Livro

        EnvConfigurator.configure_database(app, db)

    BlueprintCreator.criar_blueprints(app, APP_BLUEPRINTS)

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"errors": err.messages}), 400

    return app
