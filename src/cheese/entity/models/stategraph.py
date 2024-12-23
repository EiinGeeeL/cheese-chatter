import operator
from dataclasses import dataclass
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage

@dataclass
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
