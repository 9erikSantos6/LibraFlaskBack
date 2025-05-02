from .default_user import DefaultUser

class UserAdmin(DefaultUser):
    __tablename__ = "user_admin"

    def to_dict(self):
        return {
            "username": self.username,
            "nome": self.nome,
            "registration_timestamp": self.registration_timestamp
        }
