import os

from server import ServerConfig, ServerApp


if __name__ == "__main__":
    APP_ENVIRONMENT = os.environ.get("CONFIGURATION_SETUP", "production")
    server_config = ServerConfig[APP_ENVIRONMENT]
    gunicorn_config = server_config.GUNICORNCONFIG

    ServerApp("api:app", gunicorn_config).run()
