from app.models import DB
from sqlalchemy.orm import Mapped
from datetime import date


class Livro(DB.Model):
    id: Mapped[int] = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = DB.Column(DB.String(200), nullable=False)
    autor: Mapped[str] = DB.Column(DB.String(200), nullable=False)
    ano: Mapped[date] = DB.Column(DB.Date)
    genero: Mapped[str] = DB.Column(DB.String(50))
    sinopse: Mapped[str] = DB.Column(DB.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "sinopse": self.sinopse,
        }
