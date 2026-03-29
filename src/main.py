from fastapi import FastAPI

from src.api.routers import router


def create_app() -> FastAPI:
    app = FastAPI(title="LLM API")

    register_routes(app)

    return app


def register_routes(app: FastAPI):
    app.include_router(router)


app = create_app()
