from app.shared.extensions import DB
from app.models.users import CommonUserModel
from app.services.auth import Autenticador
from app.shared.validators.users import CommonUserValidador


class UserService:
    @staticmethod
    def registrar_user(data):
        user_valid_data = CommonUserValidador.validar_user_registration_data(data)

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
            password=user_valid_data["password"]
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
    def logar_user(data):
        validated_login_data = CommonUserValidador.validar_user_login_data(data)
        email = validated_login_data["email"]

        print(f"\n\n EMAIL RECIVED: {email}\n\n")

        user = CommonUserModel.query.filter_by(email=email).first()
        if not user:
            raise ValueError("Usuário não existe")

        senha = validated_login_data["password"]

        if not user.check_password(senha):
            raise ValueError("Credenciais inválidas")

        token = Autenticador.gerar_token(user.username, user.role)
        return {"auth_token": token} 