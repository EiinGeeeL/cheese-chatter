from langgraph.graph import StateGraph
from cheese.entity.edge import Edge

class ShouldContinueEdge(Edge):
    def condition(self, state: StateGraph) -> str:
        messages = state["messages"]
        last_message = messages[-1]
        return "continue" if last_message.tool_calls else "end"