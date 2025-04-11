from app import db
from app.models import Livro
from .livro_validations import LivroValidador


class LivroService:
    @staticmethod
    def criar_livro(data):
        dados_livro_validados = LivroValidador.validar_dados(data)
        livro = Livro(**dados_livro_validados)
        db.session.add(livro)
        db.session.commit()
        return livro

    @staticmethod
    def listar_livros():
        livros = Livro.query.all()
        return [livro.to_dict() for livro in livros]
