from dataclasses import dataclass
from typing import TypeVar
from langchain_core.runnables import Runnable

# TypeVar for the basemodel atribute refering an any LLM runnable of LangChain
LangModel = TypeVar('LangModel', bound=[Runnable])

# TypeVar for the config atributes of the entities
ConfigDataclass = TypeVar('ConfigDataclass', bound=dataclass)