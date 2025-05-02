from app.extensions import DB
from app.models.users import AdminUserModel
from app.services.auth import Autenticador

from .user_admin_validations import UserAdminValidador


class UserAdminService:
    @staticmethod
    def registrar_user_admin(data):
        user_admin_valid_data = UserAdminValidador.validate_user_admin(data)

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
    def logar_user_admin(username: str, senha: str):
        user_admin = AdminUserModel.query.filter_by(username=username).first()
        if not user_admin:
            raise ValueError("Usuário não registrado no sistema")
        
        if not user_admin.check_password(senha):
            raise ValueError("Credenciais inválidas")

        token = Autenticador.gerar_user_token(user_admin.username, user_admin.role)
        return {"auth_token": token} 
