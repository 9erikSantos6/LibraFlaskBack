from app import create_app
from dotenv import dotenv_values

envconfig = dotenv_values(".env")
if envconfig["PORT"] is None:
    raise ValueError("PORT not set in .env file")
PORT = int(envconfig["PORT"])
if PORT < 1024 or PORT > 65535:
    raise ValueError("PORT must be between 1024 and 65535")

app = create_app()


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
    )
