from typing import Any

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
from starlette.exceptions import HTTPException as StarletteHTTPException

from application.controllers import Controller

from .exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
    unhandled_error_exception_handler,
)

API_V1_PREFIX = "/api/v1"


class WebapiConfig(BaseModel):
    title: str
    version: str
    root_path: str = Field(
        None,
        description="Path prefix used by the proxy server this app is mounted behind.",
    )


def add_healthcheck_api(app: FastAPI, version: str):
    class HealthResponse(BaseModel):
        version: str

    def handler():
        return HealthResponse(version=version)

    app.add_api_route(
        path="/health",
        endpoint=handler,
        summary="Health check",
        response_model=HealthResponse,
    )


def create_app(logger: Any, controller: Controller, config: WebapiConfig):
    app = FastAPI(title=config.title, version=config.version, root_path=config.root_path or "")

    add_healthcheck_api(app, config.version)

    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_error_exception_handler)

    return app
