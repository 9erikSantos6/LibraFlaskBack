from sqlalchemy.orm import Mapped
from sqlalchemy import Column, String

from .user_model import UserModel, UserRoleEnum

class CommonUserModel(UserModel):
    __tablename__ = "user"

    email: Mapped[str] = Column(String(120), unique=True, nullable=False)

    def __init__(self, **kwargs):
        # Define role como USER automaticamente
        kwargs['_role'] = UserRoleEnum.USER
        super().__init__(**kwargs)

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "email": self.email,
            "role": self._role,
            "registration_timestamp": self.registration_timestamp
        }
