import importlib

from flask import Flask

class BlueprintCreator:
    @staticmethod
    def import_blueprint(module_name, blueprint_name):
        try:
            module = importlib.import_module(module_name)
            blueprint = getattr(module, blueprint_name)
            return blueprint
        except ImportError as e:
            raise f"Erro ao importar o módulo {module_name}: {e}"
        except AttributeError as e:
            raise f"Erro ao obter o blueprint {blueprint_name} em {module_name}: {e}"

    @staticmethod
    def criar_blueprints(app: Flask, blueprints: list[tuple[str, str]]):
        for module_name, blueprint_name in blueprints:
            blueprint = BlueprintCreator.import_blueprint(module_name, blueprint_name)
            if blueprint:
                app.register_blueprint(blueprint)