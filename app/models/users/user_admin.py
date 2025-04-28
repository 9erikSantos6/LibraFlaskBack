from sqlalchemy.orm import Mapped
from werkzeug.security import generate_password_hash, check_password_hash

from app import DB


class UserAdmin(DB.Model):
    __tablename__ = "user_admin"

    username: Mapped[str] = DB.Column(DB.String(20), primary_key=True)
    nome: Mapped[str] = DB.Column(DB.String(80), nullable=False)
    email: Mapped[str] = DB.Column(DB.String(120), unique=True, nullable=False)
    password: Mapped[str] = DB.Column(DB.String(100), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "email": self.email,
        }
