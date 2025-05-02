import string
import secrets

from flask import Flask
from config import EnvConfigType
from sqlalchemy import text, inspect
from flask_sqlalchemy import SQLAlchemy

from app.config.environment import EnvConfigurator


class DatabaseConfigurator:
    @staticmethod
    def init_db(app: Flask, db: SQLAlchemy):
        from app import models

        if EnvConfigurator.get_env_name() != EnvConfigType.PRODUCTION:
            db.create_all()
        
        DatabaseConfigurator._aplicar_db_triggers(db)

        if EnvConfigurator.criar_admin_padrao_definido():
            DatabaseConfigurator._criar_admin_padrao(db)

    @staticmethod
    def _aplicar_db_triggers(db: SQLAlchemy):
        inspector = inspect(db.engine)

        with db.engine.connect() as conn:
            # Verifica e cria trigger para user_admin
            if "user_admin" in inspector.get_table_names():
                conn.execute(text("""
                    CREATE TRIGGER IF NOT EXISTS prevent_registration_timestamp_update
                    BEFORE UPDATE OF registration_timestamp ON user_admin
                    BEGIN
                        SELECT RAISE(ABORT, 'A coluna registration_timestamp não pode ser alterada.');
                    END;
                """))

            # Verifica e cria trigger para user
            if "user" in inspector.get_table_names():
                conn.execute(text("""
                    CREATE TRIGGER IF NOT EXISTS prevent_registration_timestamp_update_user
                    BEFORE UPDATE OF registration_timestamp ON user
                    BEGIN
                        SELECT RAISE(ABORT, 'A coluna registration_timestamp não pode ser alterada.');
                    END;
                """))
    @staticmethod
    def _criar_admin_padrao(db: SQLAlchemy):
        from app.models.users.admin_user_model import AdminUserModel

        if not AdminUserModel.query.filter_by(username="admin").first():
            chars = string.ascii_letters + string.digits
            random_passowd = ''.join(secrets.choice(chars) for _ in range(8))

            admin = AdminUserModel(
                username="admin", 
                nome="Default Admin User",
                password = random_passowd
            )
            db.session.add(admin)
            db.session.commit()

            print(f"\n[SERVER_ADMIN] Default admin user: {admin.username}")
            print(f"[SERVER_ADMIN] Default admin password: {random_passowd}\n")

