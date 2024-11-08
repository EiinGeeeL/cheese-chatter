from pydantic import BaseModel, Field


class EvolutionToolInput(BaseModel):
    """
    Input for the EvolutionTool
    """
    pokemon_name: str = Field(description="a pokemon name given by the user")
