import os
import json

from flask import Flask
from flask_cors import CORS
from config import BASE_DIR
from app.config.environment import EnvConfigurator


class CORSConfigurator:
    _CONFIG_PATH = os.path.join(BASE_DIR, "cors.config.json")
    CORS_COMMON_CONFIG = {
        "resources": {"/*": {"origins": ["*"]}},
        "origins": ["*"],
        "supports_credentials": True,
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"],
        "max_age": 3600,
    }

    @staticmethod
    def _verify_config_json(cors_config: dict, env_name: str):
        REQUIRED_FIELDS = [
            "resources",
            "supports_credentials",
            "allow_headers",
            "expose_headers",
            "max_age",
        ]
        for field in REQUIRED_FIELDS:
            if field not in cors_config:
                print(
                    f"[CORS WARNING] Campo '{field}' ausente na configuração do ambiente: '{env_name}'"
                )

    @staticmethod
    def _load_config_file() -> dict:
        try:
            with open(CORSConfigurator._CONFIG_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: {CORSConfigurator._CONFIG_PATH}"
            )
        except json.JSONDecodeError:
            raise ValueError(
                f"\nErro ao decodificar o arquivo de configuração JSON: {CORSConfigurator._CONFIG_PATH}"
                f"\n - Verifique se o arquivo está formatado corretamente."
            )

    @staticmethod
    def _get_environment_config(env_name: str):
        env_name = env_name.lower()

        try:
            all_configs = CORSConfigurator._load_config_file()
        except Exception as e:
            print(f"[CORS ERROR] Falha ao carregar arquivo de configuração: {e}")
            print("[CORS WARNING] Usando configuração padrão.")
            return CORSConfigurator.CORS_COMMON_CONFIG

        # Garante que sempre exista uma configuração 'default'
        all_configs.setdefault("default", CORSConfigurator.CORS_COMMON_CONFIG)

        # Retorna a config do ambiente, ou a default como fallback
        return all_configs.get(env_name, all_configs["default"])

    @staticmethod
    def configure_cors(app: Flask):
        """
        Aplica a configuração de CORS no app.
        """
        env_name = EnvConfigurator.get_env_name()
        cors_config = CORSConfigurator._get_environment_config(env_name)

        # fallback interno para garantir que recursos/origins sempre existam
        resources = cors_config.get(
            "resources", {"/*": {"origins": cors_config.get("origins", ["*"])}}
        )

        CORSConfigurator._verify_config_json(cors_config, env_name)

        CORS(
            app,
            resources=resources,
            supports_credentials=cors_config.get("supports_credentials", True),
            allow_headers=cors_config.get("allow_headers", ["Content-Type"]),
            expose_headers=cors_config.get("expose_headers", []),
            max_age=cors_config.get("max_age", 3600),
        )


        print(f"[CORS] Configurado para: {env_name}")
        print(f"[CORS] Configurações: \n{json.dumps(cors_config, indent=2)}\n")
