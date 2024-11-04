from pydantic import BaseModel, Field

## EvolutionToolInput
class EvolutionToolInput(BaseModel):
    pokemon_name: str = Field(description="a pokemon name given by the user")