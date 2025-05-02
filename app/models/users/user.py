from sqlalchemy.orm import Mapped
from sqlalchemy import Column, String
from .default_user import DefaultUser

class User(DefaultUser):
    __tablename__ = "user"

    email: Mapped[str] = Column(String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "email": self.email,
            "registration_timestamp": self.registration_timestamp
        }
