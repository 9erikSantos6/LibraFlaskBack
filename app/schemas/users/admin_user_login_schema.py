from marshmallow import fields, validates, ValidationError
from .default_user_login_schema import DefaultUserLoginSchema

class AdminUserLoginSchema(DefaultUserLoginSchema):
    username = fields.Str(
        required=True,
        validate=lambda x: 4 <= len(x) <= 25,
        error_messages={
            "required": "Nome de usuário é obrigatório.",
            "validator_failed": "Nome de usuário deve ter de 4 a 20 caracteres.",
            "null": "Nome de usuário não pode ser nulo.",
        },
        nullable=False,
    ) 

    @validates
    def validar_username_minusculo(valor):
        if any(char.isupper() for char in valor):
            raise ValidationError("O campo 'username' não pode conter letras maiúsculas")