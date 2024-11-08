from langchain_core.runnables import Runnable
from typing import TypeVar

# TypeVar for the basemodel atribute refering an any LLM runnable of LangChain
LangModel = TypeVar('LangModel', bound=[Runnable])