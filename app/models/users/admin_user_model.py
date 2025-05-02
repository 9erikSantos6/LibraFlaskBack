from .user_model import UserModel, UserRoleEnum

class AdminUserModel(UserModel):
    __tablename__ = "user_admin"

    def __init__(self, **kwargs):
        # Define role como ADMIN automaticamente
        kwargs["_role"] = UserRoleEnum.ADMIN
        super().__init__(**kwargs)

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "registration_timestamp": self.registration_timestamp
        }
