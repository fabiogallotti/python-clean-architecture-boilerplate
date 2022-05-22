import http
from typing import Mapping

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.adapters.errors.http_errors import JsonApiError, JsonApiErrors


def http_error_phrase(status_code: int) -> str:
    return http.HTTPStatus(status_code).phrase


def format_error_response(status: str, message: str = None, code: str = None) -> Mapping:
    error = JsonApiError(status=status, title=http_error_phrase(status), detail=message, code=code)
    return JsonApiErrors(errors=[error]).dict()


async def http_exception_handler(request, exc):
    status_code = exc.status_code or 500
    error_message = exc.detail or str(exc)
    error_content = format_error_response(status=status_code, message=error_message)
    return JSONResponse(content=jsonable_encoder(error_content), status_code=status_code)


def request_validator_exception_handler():
    async def handler(request, exc):
        status_code = 422
        try:
            error_message = "; ".join(err["msg"] for err in exc.errors())
        except (AttributeError, IndexError):
            error_message = None
        error_message = error_message or "Request validation error"
        error_content = format_error_response(status=status_code, message=error_message)
        return JSONResponse(content=jsonable_encoder(error_content), status_code=status_code)

    return handler


def unhandled_error_handler():
    async def handler(request, exc):
        status_code = 500
        error_content = format_error_response(status=status_code, message="Something went wrong")
        return JSONResponse(content=jsonable_encoder(error_content), status_code=status_code)

    return handler
