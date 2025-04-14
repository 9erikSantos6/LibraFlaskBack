import importlib
import os 

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from config import ConfigType

from .config.blueprints import BLUEPRINTS


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    config_name =   os.getenv("FLASK_ENV", "default").upper()
    if config_name not in ConfigType.__members__:
        raise ValueError(f"Invalid environment name: {config_name}")
    app.config.from_object(ConfigType[config_name].value)

    db.init_app(app)

    for module_name, blueprint_name in BLUEPRINTS:
        module = importlib.import_module(module_name)
        blueprint = getattr(module, blueprint_name)
        app.register_blueprint(blueprint)

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"errors": err.messages}), 400

    if config_name != ConfigType.PRODUCTION.name:
        with app.app_context():
            db.create_all()

    return app
