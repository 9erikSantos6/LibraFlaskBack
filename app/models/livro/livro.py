from datetime import date
from typing import TYPE_CHECKING
from app.shared.extensions import DB
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import ForeignKey, Column, Integer, String, Text, Date


if TYPE_CHECKING: from app.models.users import CommonUserModel


class LivroModel(DB.Model):
    __tablename__ = "livro"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = Column(String(200), nullable=False)
    autor: Mapped[str] = Column(String(200), nullable=False)
    ano: Mapped[date] = Column(Date)
    genero: Mapped[str] = Column(String(50))
    sinopse: Mapped[str] = Column(Text)
    usuario_username: Mapped[str] = Column(String(20), ForeignKey("user.username"), nullable=False)
    usuario: Mapped["CommonUserModel"] = relationship("CommonUserModel", back_populates="livros")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "sinopse": self.sinopse,
        }
