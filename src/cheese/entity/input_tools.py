from dataclasses import dataclass
from pydantic import BaseModel, Field

dataclass(frozen=True)
class EvolutionToolInput(BaseModel):
    pokemon_name: str = Field(description="a pokemon name given by the user")