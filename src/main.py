import logging
from types import SimpleNamespace

from mangum import Mangum

from application.adapters.web import fastapi
from application.config import load
from application.controllers import Controller, ControllerConfig


def service():
    logger = None
    try:
        config = load()

        logging.basicConfig(
            level=config.logging["level"], format="%(asctime)s [%(levelname)s] %(message)s"
        )
        logger = logging.getLogger(__name__)
        logger.info("Loaded config", config=config.__dict__)

        controller_conf = ControllerConfig()
        controller = Controller(logger=logger, config=controller_conf)

        api_conf = fastapi.WebapiConfig(**config.web_api, version=config.app["version"])
        api = fastapi.create_app(logger=logger, config=api_conf, controller=controller)

        return SimpleNamespace(api=api)
    except Exception as err:
        return err


handlers = service()

asgi_app = handlers.api
handler_api = Mangum(asgi_app, lifespan="off")
logging.getLogger("mangum.http").setLevel("ERROR")
