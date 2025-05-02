from marshmallow import ValidationError, Schema, validates_schema, pre_load, fields
from bleach import clean


class DefaultUserSchema(Schema):
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

    nome = fields.Str(
        required=True,
        validate=lambda x: 2 <= len(x) <= 80,
        error_messages={
            "required": "Nome é obrigatório.",
            "validator_failed": "Nome deve ter de 2 a 80 caracteres.",
            "null": "Nome não pode ser nulo.",
        },
        nullable=False,
    )

    password = fields.Str(
        required=True,
        validate=lambda x: 6 <= len(x) <= 100,
        error_messages={
            "required": "Senha é obrigatória.",
            "validator_failed": "Senha deve ter de 6 a 100 caracteres.",
            "null": "Senha não pode ser nula.",
        },
        load_only=True,
        nullable=False,
    )

    password_confirmation = fields.Str(
        required=True,
        validate=lambda x: 6 <= len(x) <= 100,
        error_messages={
            "required": "Confirmação de senha é obrigatória.",
            "validator_failed": "Confirmação de senha deve ter de 6 a 100 caracteres.",
            "null": "Confirmação de senha não pode ser nula.",
        },
        load_only=True,
        nullable=False,
    )

    @validates_schema
    def validate_password_confirmation(self, data, **kwargs):
        if data.get("password") != data.get("password_confirmation"):
            raise ValidationError(
                "As senhas não coincidem.", field_name="password_confirmation"
            )

    @pre_load
    def sanitize_input(self, data, **kwargs):
        """
        Sanitize input data to prevent XSS attacks.
        """
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = clean(value, strip=True)
        return data
