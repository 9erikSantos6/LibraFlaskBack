from flask import Blueprint, jsonify, request
from app.services import LivroService

livro_bp = Blueprint("livros", __name__, url_prefix="/livros")


@livro_bp.route("/", methods=["GET"])
def get_livros():
    livros = LivroService.listar_livros()
    if not livros:
        return jsonify({"message": "Nenhum livro encontrado."}), 404
    return jsonify(livros), 200


@livro_bp.route("/adicionar", methods=["POST"])
def add_livro():
    data = request.get_json()
    try:
        livro = LivroService.criar_livro(data)
        return jsonify(livro.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
