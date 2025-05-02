import os
from jwt import jwt
from datetime import datetime, timedelta, timezone

from app.shared.enums import UserRoleEnum


class Autenticador:
    @staticmethod
    def autenticar(token):
        try:
            payload = jwt.decode(
                token, os.getenv("SERVER_SECRET_KEY"), algorithms=["HS256"]
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")
        except Exception as e:
            raise ValueError(f"Erro ao decodificar o token: {str(e)}")

    @staticmethod
    def gerar_token(subject: str, expires_in=3600):
        payload = {
            "sub": subject,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in),
        }
        token = jwt.encode(payload, os.getenv("SERVER_SECRET_KEY"), algorithm="HS256")
        return token
    
    @staticmethod
    def gerar_user_token(subject: str, role: UserRoleEnum,  expires_in=3600):
        payload = {
            "sub": subject,
            "role": role.value,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in),
        }
        token = jwt.encode(payload, os.getenv("SERVER_SECRET_KEY"), algorithm="HS256")
        return token
