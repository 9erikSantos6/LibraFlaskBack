from marshmallow import Schema, fields


class LivroSchema(Schema):
    id = fields.Int(dump_only=True)

    titulo = fields.Str(
        required=True,
        validate=lambda x: 2 <= len(x) <= 200,
        error_messages={
            "required": "Título é obrigatório.",
            "validator_failed": "Título deve ter de 2 a 200 caracteres.",
            "null": "Título não pode ser nulo.",
        },
    )

    autor = fields.Str(
        required=True,
        validate=lambda x: 2 <= len(x) <= 200,
        error_messages={
            "required": "Autor é obrigatório.",
            "validator_failed": "Autor deve ter no de 2 a 200 caracteres.",
            "null": "Autor não pode ser nulo.",
        },
        nuable=False,
    )

    ano = fields.Date(
        format="%Y-%m-%d",
        error_messages={"invalid": "Data deve estar no formato YYYY-MM-DD."},
    )

    genero = fields.Str(
        validate=lambda x: 2 <= len(x) <= 50,
        error_messages={"validator_failed": "Gênero deve ter de 2 a 200 caracteres."},
    )

    sinopse = fields.Str(
        validate=lambda x: 2 <= len(x) <= 500,
        error_messages={"validator_failed": "Sinopse deve ter de 2 a 500 caracteres."},
    )
