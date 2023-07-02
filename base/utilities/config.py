import os
from urllib.parse import quote_plus


class BaseApiConfig():
    DB_ADDRESS: str = os.environ["DB_ADDRESS"]
    DB_PORT: str = os.environ.get("DB_PORT", 5432)
    DB_NAME: str = os.environ["DB_NAME"]
    DB_USER: str = os.environ["DB_USER"]
    DB_PASSWORD: str = quote_plus(os.environ["DB_PASSWORD"])

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_CONFIG = {}


class DevApiConfig(BaseApiConfig):
    pass


class ProdApiConfig(BaseApiConfig):
    pass


class TestApiConfig(BaseApiConfig):
    pass


ApiConfigDict = {
    "develop": DevApiConfig,
    "production": ProdApiConfig,
    "test": TestApiConfig
}

ApiConfig = ApiConfigDict.get(
    os.environ.get("CONFIGURATION_SETUP", "production"),
    "production"
)
