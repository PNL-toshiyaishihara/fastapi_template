"""
main application
"""
from fastapi import FastAPI

from base.utilities import LoggingMiddleware
from base.database import AsyncDatabaseSession


def create_app():
    app = FastAPI()
    app.add_middleware(LoggingMiddleware)

    @app.on_event("startup")
    async def startup_event():
        app.AsyncSession = AsyncDatabaseSession()

    @app.on_event("shutdown")
    async def shutdown_event():
        if hasattr(app, "AsyncSession"):
            app.AsyncSession.cleanup()

    return app
