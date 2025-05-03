from app.schemas.users.default_user_registration_schema import DefaultUserSchema


class AdminUserRegistrationSchema(DefaultUserSchema):
    """
    Schema for user admin operations.
    Inherits from UserDefaultSchema to include common user fields.
    """

    # Additional fields specific to admin operations can be added here
    # For example, you might want to add a field for user roles or permissions
    # role = fields.Str(required=True, validate=validate.Length(min=1))
    pass
