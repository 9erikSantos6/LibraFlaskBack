from flask import Blueprint, jsonify, request
from app.services.users import UserAdminService


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/login", methods=["POST"])
def admin_login():
    data = request.get_json()

    try:
        admin_login_token = UserAdminService.logar_user_admin(data)
        return jsonify(admin_login_token), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 406
    
@admin_bp.route("/registrar", methods=["POST"])
def registrar_admin():
    data = request.get_json()

    try:
        admin_registration_confirmation = UserAdminService.registrar_user_admin(data)
        return jsonify(admin_registration_confirmation), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 406
