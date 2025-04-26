import time
import os
from app import create_app
from app.config import CORSConfigurator


app = create_app()

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        # Isso só roda no subprocesso principal real
        CORSConfigurator.configure_cors(app)

    app.run(
        debug=app.config["DEBUG"],
        port=app.config["SERVER_PORT"],
    )
