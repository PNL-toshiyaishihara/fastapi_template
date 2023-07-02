import os


class BaseServerConfig():
    GUNICORNCONFIG = {
        "bind": "{}:{}".format(
            os.environ.get("SERVER_HOST", "0.0.0.0"),
            int(os.environ.get("SERVER_PORT", 80))
        ),
        "worker_class": "uvicorn.workers.UvicornWorker"
    }


class DevServerConfig(BaseServerConfig):
    GUNICORNCONFIG = {
        "bind": "{}:{}".format(
            os.environ.get("SERVER_HOST", "0.0.0.0"),
            int(os.environ.get("SERVER_PORT", 80))
        ),
        "worker_class": "uvicorn.workers.UvicornWorker",
        "reload": True,
        "loglevel": "debug"
    }


class ProdServerConfig(BaseServerConfig):
    GUNICORNCONFIG = {
        "bind": "{}:{}".format(
            os.environ.get("SERVER_HOST", "0.0.0.0"),
            int(os.environ.get("SERVER_PORT", 80))
        ),
        "worker_class": "uvicorn.workers.UvicornWorker"
    }


class TestServerConfig(BaseServerConfig):
    GUNICORNCONFIG = {
        "bind": "{}:{}".format(
            os.environ.get("SERVER_HOST", "0.0.0.0"),
            int(os.environ.get("SERVER_PORT", 80))
        ),
        "worker_class": "uvicorn.workers.UvicornWorker",
        "reload": True
    }


ServerConfig = {
    "develop": DevServerConfig,
    "production": ProdServerConfig,
    "test": TestServerConfig
}
