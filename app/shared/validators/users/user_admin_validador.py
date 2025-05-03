from app.schemas.users import AdminUserRegistrationSchema
from app.schemas.users import AdminUserLoginSchema


class UserAdminValidador:
    @staticmethod
    def validar_admin_user_registration_data(data):
        admin_registration_schema = AdminUserRegistrationSchema()
        return admin_registration_schema.load(data)
    
    def validar_admin_user_login_data(data):
        admin_login_schema = AdminUserLoginSchema()
        return admin_login_schema.load(data)


