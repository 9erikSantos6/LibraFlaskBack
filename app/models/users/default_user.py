from app import DB
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped
from sqlalchemy import DateTime, Column, String
from werkzeug.security import generate_password_hash, check_password_hash

class DefaultUser(DB.Model):
    __abstract__ = True

    username: Mapped[str] = Column(String(20), primary_key=True, nullable=False)
    nome: Mapped[str] = Column(String(80), nullable=False)
    password: Mapped[str] = Column(String(100), nullable=False)
    registration_timestamp: Mapped[datetime] = Column(
        DateTime(), 
        nullable=False, 
        default=lambda: datetime.now(timezone.utc)
        )
    
    def __setattr__(self, name, value):
        # Protege contra alterações no campo após a criação
        if (
            name == "registration_timestamp"
            and hasattr(self, "registration_timestamp")
        ):
            raise AttributeError("registration_timestamp não pode ser modificado")
        super().__setattr__(name, value)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "registration_timestamp": self.registration_timestamp
        }
