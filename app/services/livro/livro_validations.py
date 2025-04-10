from datetime import datetime


class LivroValidador:
    @staticmethod
    def validar_dados(data):
        """
        Valida os dados do livro.
        :param data: dicionário com os dados do livro

        :return: True se os dados forem válidos, False caso contrário
        """
        required = ["titulo", "autor"]
        if not all(k in data for k in required):
            raise ValueError("Dados incompletos")

        if "titulo" in data and len(data["titulo"]) > 200:
            raise ValueError("Título muito longo")
        if "autor" in data and len(data["autor"]) > 200:
            raise ValueError("Autor muito longo")
        if "ano" in data and isinstance(data["ano"], str):
            try:
                data["ano"] = datetime.strptime(data["ano"], "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Formato de data inválido. Use YYYY-MM-DD.")
        if "genero" in data and len(data["genero"]) > 50:
            raise ValueError("Gênero muito longo")
        if "sinopse" in data and len(data["sinopse"]) > 500:
            raise ValueError("Sinopse muito longa")
        return True
