from flask import Blueprint, jsonify, request
from app.models import Livro

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hi, human!"})
