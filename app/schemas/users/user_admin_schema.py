from marshmallow import fields, Schema, pre_load
from bleach import clean

from .default_schema import UserDefaultSchema

class UserAdminSchema(UserDefaultSchema):
    """
    Schema for user admin operations.
    Inherits from UserDefaultSchema to include common user fields.
    """

    # Additional fields specific to admin operations can be added here
    # For example, you might want to add a field for user roles or permissions
    # role = fields.Str(required=True, validate=validate.Length(min=1))

    @pre_load
    def sanitize_input(self, data, **kwargs):
        """
        Sanitize input data to prevent XSS attacks.
        """
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = clean(value)
        return data
    
