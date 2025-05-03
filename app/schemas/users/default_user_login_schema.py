from marshmallow import Schema, pre_load, fields
from bleach import clean

class DefaultUserLoginSchema(Schema):
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

    @pre_load
    def sanitize_input(self, data, **kwargs):
        """
        Sanitize input data to prevent XSS attacks.
        """
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = clean(value, strip=True)
        return data