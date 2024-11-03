from typing import Any, Callable, Dict, Tuple
from langgraph.graph import END
from cheese.entity.config_stategraph import AgentState
from cheese.entity.edge import ConditionalEdge

class ShouldContinueEdge(ConditionalEdge):
    def edge(self, state: AgentState) -> str:
        messages = state["messages"]
        last_message = messages[-1]
        return "continue" if last_message.tool_calls else "end"