from app.schemas.users import CommonUserRegistrationSchema
from app.schemas.users import CommonUserLoginSchema


class CommonUserValidador:
    @staticmethod
    def validar_user_registration_data(data):
        user_registration_schema = CommonUserRegistrationSchema()
        return user_registration_schema.load(data)
    
    def validar_user_login_data(data):
        user_login_schema = CommonUserLoginSchema()
        return user_login_schema.load(data)