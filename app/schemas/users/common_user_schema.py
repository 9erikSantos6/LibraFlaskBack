from marshmallow import fields

from .default_user_schema import DefaultUserSchema


class CommonUserSchema(DefaultUserSchema):
    """
    Schema for user operations.
    Inherits from UserDefaultSchema to include common user fields.
    """

    # Additional fields specific to user operations can be added here
    # For example, you might want to add a field for user roles or permissions
    # role = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email é obrigatório.",
            "null": "Email não pode ser nulo.",
            "invalid": "Email inválido.",
        },
        nullable=False,
    )
    pass
