from flask import jsonify
from app import db
from app.models import Livro
from datetime import datetime


def criar_livro(data):
    required = ["titulo", "autor"]
    if not all(k in data for k in required):
        raise ValueError("Dados incompletos")

    ano = None
    if "ano" in data and data["ano"]:
        try:
            ano = datetime.strptime(data["ano"], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Formato de data inválido. Use YYYY-MM-DD"}), 400

    livro = Livro(
        titulo=data["titulo"],
        autor=data["autor"],
        ano=ano,
        genero=data.get("genero"),
        sinopse=data.get("sinopse"),
    )

    db.session.add(livro)
    db.session.commit()
    return livro
