from flask import Blueprint, jsonify, request
from app.services import LivroService

livro_bp = Blueprint("livros", __name__, url_prefix="/livros")


@livro_bp.route("/", methods=["GET"])
def get_livros():
    livros = LivroService.listar_livros()
    return jsonify(livros), 200


@livro_bp.route("/", methods=["POST"])
def add_livro():
    data = request.get_json()
    try:
        livro = LivroService.criar_livro(data)
        return jsonify(livro.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@livro_bp.route("/<int:livro_id>", methods=["GET"])
def get_livro(livro_id):
    try:
        livro = LivroService.listar_livro_por_id(livro_id)
        return jsonify(livro), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@livro_bp.route("/<int:livro_id>", methods=["PUT"])
def update_livro(livro_id):
    data = request.get_json()
    try:
        livro = LivroService.atualizar_livro(livro_id, data)
        return jsonify(livro), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@livro_bp.route("/<int:livro_id>", methods=["PATCH"])
def update_livro_parcial(livro_id):
    data = request.get_json()
    try:
        livro = LivroService.atualizar_livro_parcial(livro_id, data)
        return jsonify(livro), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@livro_bp.route("/<int:livro_id>", methods=["DELETE"])
def delete_livro(livro_id):
    try:
        response = LivroService.deletar_livro(livro_id)
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


"""
#   AINDA NÃO IMPLEMENTADO

@livro_bp.route("/search", methods=["GET"])
def search_livros():
    # Endpoint para buscar livros com base em filtros e ordenação

    try:
        filtros = request.args.to_dict()
        livros = LivroService.buscar_livros(filtros)

        if not livros:
            return jsonify({"message": "Nenhum livro encontrado."}), 404

        return jsonify(livros), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
"""
