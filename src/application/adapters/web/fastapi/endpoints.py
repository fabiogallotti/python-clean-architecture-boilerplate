from fastapi import APIRouter, Path
from fastapi.routing import APIRoute
from pydantic.main import BaseModel

from application.adapters.web.fastapi.exceptions import JsonApiErrors
from application.controllers import Controller


class TestResponse(BaseModel):
    data: str


def route_test(controller: Controller):
    def endpoint(
        id: str = Path(..., description="id"),
    ):
        res = controller.test(id=id)
        return TestResponse(data=res)

    return APIRoute(
        path="/test",
        endpoint=endpoint,
        status_code=200,
        response_model=TestResponse,
        methods=["GET"],
        summary="test",
        responses={
            400: {"model": JsonApiErrors, "description": "Bad Request."},
            422: {"model": JsonApiErrors, "description": "Validation Error."},
            500: {"model": JsonApiErrors, "description": "Internal server error."},
        },
    )


def router(controller: Controller):
    return APIRouter(
        routes=[
            route_test(controller),
        ]
    )
