from app.shared.extensions import DB
from datetime import date
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, Text, Date


class LivroModel(DB.Model):
    __tablename__ = "livro"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = Column(String(200), nullable=False)
    autor: Mapped[str] = Column(String(200), nullable=False)
    ano: Mapped[date] = Column(Date)
    genero: Mapped[str] = Column(String(50))
    sinopse: Mapped[str] = Column(Text)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "sinopse": self.sinopse,
        }
