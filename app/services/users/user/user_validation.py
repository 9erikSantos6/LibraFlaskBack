from app.schemas import CommonUserSchema


class CommonUserValidador:
    @staticmethod
    def validate_user(data):
        user_schema = CommonUserSchema()
        return user_schema.load(data)