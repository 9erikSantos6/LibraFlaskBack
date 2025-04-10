from app import db
from app.models import Livro
from .livro_validations import LivroValidador


class LivroService:
    @staticmethod
    def criar_livro(data):
        LivroValidador.validar_dados(data)

        livro = Livro(
            titulo=data["titulo"],
            autor=data["autor"],
            ano=data.get("ano"),
            genero=data.get("genero"),
            sinopse=data.get("sinopse"),
        )

        db.session.add(livro)
        db.session.commit()
        return livro

    @staticmethod
    def listar_livros():
        livros = Livro.query.all()
        return [livro.to_dict() for livro in livros]
