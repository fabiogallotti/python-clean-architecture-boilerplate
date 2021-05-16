from types import SimpleNamespace

from application.config import load


def service():
    try:
        load()
        return SimpleNamespace()
    except Exception as err:
        return err


handlers = service()
