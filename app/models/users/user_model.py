from app.extensions import DB
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped
from datetime import datetime, timezone
from sqlalchemy import DateTime, Column, String, Enum as SQLAEnum
from werkzeug.security import generate_password_hash, check_password_hash

class UserRoleEnum(PyEnum):
    ADMIN = "admin"
    USER = "user"

class UserModel(DB.Model):
    __abstract__ = True

    username: Mapped[str] = Column(String(20), primary_key=True, nullable=False)
    nome: Mapped[str] = Column(String(80), nullable=False)
    _role: Mapped[UserRoleEnum] = Column("role", SQLAEnum(UserRoleEnum), nullable=False)
    _password: Mapped[str] = Column("password", String(100), nullable=False)
    registration_timestamp: Mapped[datetime] = Column(
        DateTime(timezone=True), 
        nullable=False, 
        default=lambda: datetime.now(timezone.utc)
    )

    def __setattr__(self, name, value):
        # Protege contra alterações no campo após a criação
        if name == "registration_timestamp" and hasattr(self, "registration_timestamp"):
            raise AttributeError("registration_timestamp não pode ser modificado")

        super().__setattr__(name, value)

    @property
    def password(self):
        raise AttributeError("Acesso direto ao campo 'password' não é permitido. Use 'set_password'.")

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("A senha não pode ser vazia.")
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def to_dict(self):
        raise NotImplementedError("Implemente to_dict()")
