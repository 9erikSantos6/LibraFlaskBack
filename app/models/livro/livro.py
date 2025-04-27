from app import db
from sqlalchemy.orm import Mapped
from datetime import date


class Livro(db.Model):
    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = db.Column(db.String(200), nullable=False)
    autor: Mapped[str] = db.Column(db.String(200), nullable=False)
    ano: Mapped[date] = db.Column(db.Date)
    genero: Mapped[str] = db.Column(db.String(50))
    sinopse: Mapped[str] = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "sinopse": self.sinopse,
        }
