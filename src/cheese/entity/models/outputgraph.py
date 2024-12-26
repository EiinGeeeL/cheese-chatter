from dataclasses import dataclass
from pydantic import BaseModel
from typing import Any


@dataclass
class OutputState(BaseModel): 
    """Defines the output state, representing a narrower interface to the outside world.
    """
    output: Any