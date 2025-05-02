from app.extensions import DB
from app.models.users import CommonUserModel
from app.services.auth import Autenticador
from .user_validation import UserValidador


class UserService:
    @staticmethod
    def registrar_user(data):
        user_valid_data = UserValidador.validate_user(data)

        if CommonUserModel.query.filter_by(email=user_valid_data["email"]).first():
            raise ValueError("Email já está em uso.")

        if CommonUserModel.query.filter_by(username=user_valid_data["username"]).first():
            raise ValueError("Nome de usuário já está em uso.")

        if (user_valid_data["password"] != user_valid_data["password_confirmation"]):
            raise ValueError("Senha e confirmação de senha não conferem.")

        user = CommonUserModel(
            username=user_valid_data["username"],
            nome=user_valid_data["nome"],
            email=user_valid_data["email"],
            passord=user_valid_data["password"]
        )

        DB.session.add(user)
        DB.session.commit()

        confirm_user_data = {
            "username": user.username,
            "nome": user.nome,
            "email": user.email,
        }
        return {"message": "Usuário registrado com sucesso", "user": confirm_user_data}
    
    @staticmethod
    def logar_user_admin(email: str, senha: str):
        user = CommonUserModel.query.filter_by(username=email).first()
        if not user:
            raise ValueError("Usuário não registrado no sistema")
        
        if not user.check_password(senha):
            raise ValueError("Credenciais inválidas")

        token = Autenticador.gerar_user_token(user.username, user.role)
        return {"auth_token": token} 