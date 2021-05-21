from typing import List

from pydantic import BaseModel, Field


class JsonApiError(BaseModel):
    status: str = Field(None, description="HTTP status code.")
    title: str = Field(None, description="Short, human-readable summary of the problem type.")
    detail: str = Field(None, description="Human-readable explanation specific to the problem.")
    code: str = Field(None, description="Application-specific error code.")

    class Config:
        extra = "forbid"


class JsonApiErrors(BaseModel):
    errors: List[JsonApiError]

    class Config:
        extra = "forbid"
