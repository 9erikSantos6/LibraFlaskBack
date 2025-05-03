from marshmallow import fields
from .default_user_login_schema import DefaultUserLoginSchema

class CommonUserLoginSchema(DefaultUserLoginSchema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email é obrigatório.",
            "null": "Email não pode ser nulo.",
            "invalid": "Email inválido.",
        },
        nullable=False,
    )