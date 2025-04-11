from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routers import main_bp, livro_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(livro_bp)

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"errors": err.messages}), 400

    with app.app_context():
        db.create_all()

    return app
