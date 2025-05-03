from app.shared.extensions import DB
from app.models.users import AdminUserModel
from app.services.auth import Autenticador

from app.shared.validators.users import UserAdminValidador


class UserAdminService:
    @staticmethod
    def registrar_user_admin(data):
        user_admin_valid_data = UserAdminValidador.validar_admin_user_registration_data(data)

        if AdminUserModel.query.filter_by(username=user_admin_valid_data["username"]).first():
            raise ValueError("Username já cadastrado em outro usuário")

        if user_admin_valid_data["password"] != user_admin_valid_data["password_confirmation"]:
            raise ValueError("As senhas não coincidem")

        user_admin = AdminUserModel(
            username=user_admin_valid_data["username"],
            nome=user_admin_valid_data["nome"],
            password=user_admin_valid_data["password"] 
        )

        DB.session.add(user_admin)
        DB.session.commit()

        confirm_user_admin_data = {
            "username": user_admin.username,
            "nome": user_admin.nome,
        }

        return {"message": "Usuário registrado com sucesso", "user": confirm_user_admin_data}

    @staticmethod
    def logar_user_admin(data):
        validated_login_data = UserAdminValidador.validar_admin_user_login_data(data)
        username = validated_login_data["username"]

        user_admin = AdminUserModel.query.filter_by(username=username).first()
        if not user_admin:
            raise ValueError("Usuário não existe")

        senha = validated_login_data["password"]

        if not user_admin.check_password(senha):
            raise ValueError("Credenciais inválidas")

        token = Autenticador.gerar_token(user_admin.username, user_admin.role)
        return {"auth_token": token} 
