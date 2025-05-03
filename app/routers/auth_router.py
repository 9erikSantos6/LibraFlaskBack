from flask import Blueprint, jsonify, request
from app.services.users import UserService


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()

    try:
        user_login_token = UserService.logar_user(data)
        return jsonify(user_login_token), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 406


@auth_bp.route("/registrar", methods=["POST"])
def user_registration():
    data = request.get_json()

    try:
        user_registration_confirmation = UserService.registrar_user(data)
        return jsonify(user_registration_confirmation), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 406






