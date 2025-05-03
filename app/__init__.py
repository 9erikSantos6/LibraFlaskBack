from flask import Flask, jsonify
from marshmallow import ValidationError

from app.config import EnvConfigurator, DatabaseConfigurator
from app.config.blueprints import APP_BLUEPRINTS
from app.shared.utils.blueprint import BlueprintLoader
from app.shared.extensions import DB


def create_app():
    app = Flask(__name__)

    EnvConfigurator.load_app_config(app)

    DB.init_app(app)

    with app.app_context():
        DatabaseConfigurator.init_db(app, DB)

    BlueprintLoader.criar_blueprints(app, APP_BLUEPRINTS)

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"errors": err.messages}), 400

    return app
