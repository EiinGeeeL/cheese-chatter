import requests
import logging
from typing import Optional, Type
from langchain_core.tools import (
    BaseTool, 
    ToolException,
)
from langchain_core.callbacks import (
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel
from cheese.entity.config_tools import EvolutionToolConfig


class EvolutionTool(BaseTool):
    name: str = None
    description: str = None
    args_schema: Type[BaseModel] = None
    return_direct: bool = None

    # New pydantic attribute
    config: EvolutionToolConfig = None 
    logger: logging.Logger = None
     

    def __init__(self, **data):
        super().__init__(**data)
        self.config = EvolutionToolConfig()
        self.description = self.config.description
        self.args_schema = self.config.args_schema
        self.return_direct = self.config.return_direct

        self.name = self.__class__.__name__
        self.logger = logging.getLogger(self.__class__.__name__) 

    def _run(self, pokemon_name: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> list:
        """
        Run the tool logic
        """
        self.logger.info(f"Args: {pokemon_name.lower()}")

        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
        species_response = requests.get(species_url)

        if species_response.status_code != 200:
            raise ToolException(f"Error: {pokemon_name} is not a valid pokemon")
        
        species_data = species_response.json()

        # Extract evolution chain URL from species data
        evolution_chain_url = species_data['evolution_chain']['url']

        # Get the evolution chain data
        evolution_response = requests.get(evolution_chain_url)
        evolution_data = evolution_response.json()

        # Traverse the evolution chain and get the names of evolutions
        evolutions = []
        current_evolution = evolution_data['chain']
        
        while current_evolution:
            evolutions.append(current_evolution['species']['name'])
            if len(current_evolution['evolves_to']) > 0:
                current_evolution = current_evolution['evolves_to'][0]
            else:
                break
        
        return evolutions