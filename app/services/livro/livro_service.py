from app.models import LivroModel
from app.shared.extensions import DB
from app.shared.validators.livro import LivroValidador


class LivroService:
    @staticmethod
    def criar_livro(data: dict, user_username=str):
        if not data.get("usuario_username"):
            data["usuario_username"] = user_username
        dados_livro_validados = LivroValidador.validar_dados(data)
        livro = LivroModel(**dados_livro_validados)
        DB.session.add(livro)
        DB.session.commit()
        return livro

    @staticmethod
    def listar_livros(user_username=str):
        livros = LivroModel.query.filter(LivroModel.usuario_username.ilike(f"{user_username}")).all()
        return [livro.to_dict() for livro in livros]

    @staticmethod
    def listar_livro_por_id(livro_id, user_username=str):
        livro = LivroModel.query.filter_by(id=livro_id, usuario_username=user_username).first()
        if livro:
            return livro.to_dict()
        else:
            raise ValueError("Livro não encontrado")

    @staticmethod
    def atualizar_livro(livro_id, data, user_username: str):
        livro = LivroModel.query.filter_by(id=livro_id, usuario_username=user_username).first()
        if not livro:
            raise ValueError("Livro não encontrado")

        dados_livro_validados = LivroValidador.validar_dados(data)
        for key, value in dados_livro_validados.items():
            setattr(livro, key, value)

        DB.session.commit()
        return livro.to_dict()

    @staticmethod
    def deletar_livro(livro_id, user_username:str):
        livro = LivroModel.query.filter_by(id=livro_id, usuario_username=user_username).first()
        if not livro:
            raise ValueError("Livro não encontrado")

        DB.session.delete(livro)
        DB.session.commit()
        return {"message": "Livro deletado com sucesso"}

    @staticmethod
    def atualizar_livro_parcial(livro_id, data, user_username:str):
        livro = LivroModel.query.filter_by(id=livro_id, usuario_username=user_username).first()
        if not livro:
            raise ValueError("Livro não encontrado")

        for key, value in data.items():
            if hasattr(livro, key):
                setattr(livro, key, value)

        DB.session.commit()
        return livro.to_dict()

# CONTINUAR IMPLEMENTANDO USER USERNAME...
    @staticmethod
    def listar_livro_por_titulo(titulo: str, user_username: str):
        livros = LivroModel.query.filter_by(titulo=titulo, usuario_username=user_username).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o título especificado")

    @staticmethod
    def listar_livro_por_autor(autor: str, user_username: str):
        livros = LivroModel.query.filter_by(autor=autor,usuario_username=user_username).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o autor especificado")

    @staticmethod
    def listar_livro_por_genero(genero: str, user_username: str):
        livros = LivroModel.query.filter_by(genero=genero, usuario_username=user_username).all()
        if livros:
            return [livro.to_dict() for livro in livros]
        else:
            raise ValueError("Nenhum livro encontrado para o gênero especificado")

    @staticmethod
    def listar_livro_por_ano(ano: str, user_username: str):
        livros = LivroModel.query.filter_by(ano=ano, usuario_username=user_username).all()
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
