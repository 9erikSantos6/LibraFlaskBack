from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hi, human!"})
