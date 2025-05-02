from app.schemas import AdminUserSchema


class UserAdminValidador:
    @staticmethod
    def validate_user_admin(data):
        user_admin_schema = AdminUserSchema()
        return user_admin_schema.load(data)
