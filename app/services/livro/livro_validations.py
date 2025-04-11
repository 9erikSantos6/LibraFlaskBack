from app.schemas.livro import LivroSchema


class LivroValidador:
    @staticmethod
    def validar_dados(data):
        livro_schema = LivroSchema()
        return livro_schema.load(data)
