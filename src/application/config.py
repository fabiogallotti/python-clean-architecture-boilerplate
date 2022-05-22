import os
from types import SimpleNamespace

APP_NAME = "service"


def load():
    return SimpleNamespace(
        app={
            "name": APP_NAME,
            "env": os.environ["ENV"],
            "version": os.getenv("VERSION", "unknown"),
        },
        logging={
            "level": os.getenv("LOG_LEVEL", "INFO"),
        },
    )
