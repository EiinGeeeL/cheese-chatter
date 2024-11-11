from pydantic import BaseModel, Field
from typing import Type

class CustomBaseTool:
    class EvolutionToolConfig:
        class Input(BaseModel):
            """
            Input for the EvolutionTool
            """
            pokemon_name: str = Field(description="a pokemon name given by the user")

        description: str = "This is a tool to give you information about the evolution path of a certain pokemon"
        args_schema: Type[BaseModel] = Input
        return_direct: bool = True

