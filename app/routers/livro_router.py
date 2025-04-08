from flask import Blueprint, jsonify, request
from app.models import Livro
from app.services.livro_service import *

livro_bp = Blueprint("livros", __name__, url_prefix="/livros")


@livro_bp.route("/", methods=["GET"])
def get_livros():
    Livros = Livro.query.all()
    return jsonify([b.to_dict() for b in Livros])


@livro_bp.route("/adicionar", methods=["POST"])
def add_livro():
    data = request.get_json()
    try:
        livro = criar_livro(data)
        return jsonify(livro.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
