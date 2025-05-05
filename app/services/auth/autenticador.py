import os
import jwt
from datetime import datetime, timedelta, timezone

from app.shared.enums import UserRoleEnum
from app.config.environment import EnvConfigurator

env_config = EnvConfigurator.get_config()
SECRET_KEY = env_config.SERVER_SECRET_KEY

class Autenticador:
    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")
        except Exception as e:
            raise ValueError(f"Erro ao decodificar o token: {str(e)}")

    @staticmethod
    def gerar_token(subject: str, role: UserRoleEnum = None, expires_in=3600):
        payload = {
            "sub": subject,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in),
        }
        if role:
            payload["role"] = role.value

        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod 
    def obter_payload_autenticado_usuario(auth_header):
        token = Autenticador.tratar_user_token(auth_header)
        payload = Autenticador.decode_token(token)
        if not payload.get("sub"):
            raise ValueError("Você não possui autorização para acessar este recurso")
        return payload
    
    @staticmethod
    def tratar_user_token(authorization: str):
        if not authorization:
            raise ValueError("Nenhuma autorização foi envida no cabeçalho")
        if authorization.startswith("Bearer "):
            token = authorization.split(" ")[1]
        else:
            token = authorization
        return token