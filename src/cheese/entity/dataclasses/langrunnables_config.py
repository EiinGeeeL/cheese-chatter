from dataclasses import dataclass
from langchain_core.tools import BaseTool
from langchain_ollama import ChatOllama
from cheese.components.tools.evolution_tool import EvolutionTool
from cheese.utils.common import read_yaml
from cheese.constants import *
from cheese.utils.type_vars import LangModel
from typing import List


## Model Configuration
config = read_yaml(CONFIG_FILE_PATH)

# Initialize ChatOllama model
model = ChatOllama(
    model=config['ollama']['model'],
    temperature=config['ollama']['temperature'],
    # other params...
)

## ShouldContinueConfig
# @dataclass(frozen=True) # TODO Fix this with a component class model
class CheeseAgentConfig:
        model: LangModel = model
        tools: List[BaseTool] = [EvolutionTool()]

