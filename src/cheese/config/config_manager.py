from typing import Type, List
from pydantic import BaseModel
from langchain_core.tools import BaseTool
from cheese.pipeline.services.llm_services import LLMServices
from cheese.entity.models.evolution_tool_input import EvolutionToolInput
# from cheese.components.tools.evolution_tool import EvolutionTool

class ConfigManager:
    class EvolutionToolConfig:
        description: str = "This is a tool to give you information about the evolution path of a certain pokemon"
        args_schema: Type[BaseModel] = EvolutionToolInput
        return_direct: bool = True
    
    class CheeseAgentConfig:
        model: LLMServices = LLMServices.model
        # tools: List[BaseTool] = [EvolutionTool()] # TODO The origin of the cirular import