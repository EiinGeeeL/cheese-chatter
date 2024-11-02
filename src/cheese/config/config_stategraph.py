import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage

## State Definition
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]