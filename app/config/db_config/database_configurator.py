from flask import Flask
from config import EnvConfigType
from sqlalchemy import text, inspect

from flask_sqlalchemy import SQLAlchemy
from app.config.env.env_config import EnvConfigurator


class DatabaseConfigurator:
    @staticmethod
    def init_db(app: Flask, db: SQLAlchemy):
        from app import models

        if EnvConfigurator.get_env_name() != EnvConfigType.PRODUCTION.name:
            db.create_all()
        
        DatabaseConfigurator._aplicar_db_triggers(db)

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
