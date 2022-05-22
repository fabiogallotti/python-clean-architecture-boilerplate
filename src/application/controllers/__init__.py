from typing import Any

from pydantic import BaseModel, dataclasses


class ControllerConfig(BaseModel):
    pass


@dataclasses.dataclass
class Controller:
    logger: Any
    config: ControllerConfig

    def __post_init_post_parse(self):
        pass
