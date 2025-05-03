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
