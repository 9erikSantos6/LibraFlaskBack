from app import DB
from app.models import Livro
from .livro_validations import LivroValidador


class LivroService:
    @staticmethod
    def criar_livro(data):
        dados_livro_validados = LivroValidador.validar_dados(data)
        livro = Livro(**dados_livro_validados)
        DB.session.add(livro)
        DB.session.commit()
        return livro

    @staticmethod
    def listar_livros():
        livros = Livro.query.all()
        return [livro.to_dict() for livro in livros]

    @staticmethod
    def listar_livro_por_id(livro_id):
        livro = Livro.query.get(livro_id)
        if livro:
            return livro.to_dict()
        else:
            raise ValueError("Livro não encontrado")

    @staticmethod
    def atualizar_livro(livro_id, data):
        livro = Livro.query.get(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado")

        dados_livro_validados = LivroValidador.validar_dados(data)
        for key, value in dados_livro_validados.items():
            setattr(livro, key, value)

        DB.session.commit()
        return livro.to_dict()

    @staticmethod
    def deletar_livro(livro_id):
        livro = Livro.query.get(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado")

        DB.session.delete(livro)
        DB.session.commit()
        return {"message": "Livro deletado com sucesso"}

    @staticmethod
    def atualizar_livro_parcial(livro_id, data):
        livro = Livro.query.get(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado")

        for key, value in data.items():
            if hasattr(livro, key):
                setattr(livro, key, value)

        DB.session.commit()
        return livro.to_dict()

    @staticmethod
    def listar_livro_por_titulo(titulo: str):
        livros = Livro.query.filter(Livro.titulo.ilike(f"%{titulo}%")).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o título especificado")

    @staticmethod
    def listar_livro_por_autor(autor: str):
        livros = Livro.query.filter_by(autor=autor).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o autor especificado")

    @staticmethod
    def listar_livro_por_genero(genero: str):
        livros = Livro.query.filter_by(genero=genero).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o gênero especificado")

    @staticmethod
    def listar_livro_por_ano(ano: str):
        livros = Livro.query.filter_by(ano=ano).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o ano especificado")

    """ 
        AINDA NÃO IMPLEMENTADO
        Endpoint para buscar livros com base em filtros e ordenação.

    @staticmethod
    def buscar_livros(filtros: dict):
        query = Livro.query

        # Campos separados por tipo de filtro
        campos_ilike = {"titulo", "autor", "genero", "sinopse"}
        campos_igualdade = {"ano"}

        # Separar paginação e ordenação
        sort = filtros.pop("sort", None)
        page = int(filtros.pop("page", 1))
        per_page = int(filtros.pop("per_page", 10))

        # Aplicar filtros dinamicamente
        for campo, valor in filtros.items():
            if campo in campos_ilike:
                if valor and isinstance(valor, str) and valor.strip():
                    query = query.filter(
                        getattr(Livro, campo).ilike(f"%{valor.strip()}%")
                    )
            elif campo in campos_igualdade:
                try:
                    query = query.filter(getattr(Livro, campo) == int(valor))
                except (ValueError, TypeError):
                    raise ValueError(f"Valor inválido para o campo {campo}.")
            else:
                raise ValueError(f"Campo inválido: {campo}")

        # Aplicar ordenação
        if sort:
            try:
                campo_sort, direcao = sort.rsplit("_", 1)
                if campo_sort not in campos_ilike.union(
                    campos_igualdade
                ) or direcao not in {"asc", "desc"}:
                    raise ValueError("Parâmetro de ordenação inválido.")
                coluna = getattr(Livro, campo_sort)
                query = query.order_by(
                    coluna.asc() if direcao == "asc" else coluna.desc()
                )
            except ValueError:
                raise ValueError(
                    "Formato de sort inválido. Use 'campo_asc' ou 'campo_desc'."
                )

        # Paginação
        livros_paginados = query.paginate(page=page, per_page=per_page, error_out=False)
        return [livro.to_dict() for livro in livros_paginados.items]
    """
