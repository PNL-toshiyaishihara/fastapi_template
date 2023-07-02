from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine
)
from sqlalchemy.orm import sessionmaker

from base.utilities import ApiConfig


class AsyncDatabaseSession():
    def __init__(self):
        self._engine: AsyncEngine = create_async_engine(
            ApiConfig.SQLALCHEMY_DATABASE_URI
        )
        self.AsyncSessionFactory = sessionmaker(
            self._engine,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def get_db(self) -> AsyncGenerator:
        async with self.AsyncSessionFactory() as session:
            yield session
