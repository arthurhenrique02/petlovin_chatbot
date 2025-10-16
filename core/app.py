from dotenv import load_dotenv
from fastapi import FastAPI

from core.config import config_routes

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(title="Petlovin chatbot", version="1.0.0")

    config_routes(app)

    return app


app = create_app()
