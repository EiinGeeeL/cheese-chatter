from dataclasses import dataclass
from pydantic import BaseModel
from typing import Type
from cheese.entity.config_input_tools import EvolutionToolInput

## EvolutionToolConfig
@dataclass(frozen=True)
class EvolutionToolConfig:
    description: str = "This is a tool to give you a information of the evolution path of a certain pokemon"
    args_schema: Type[BaseModel] = EvolutionToolInput
    return_direct: bool = True
