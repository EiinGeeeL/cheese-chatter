from langgraph.graph import StateGraph
from cheese.entity.statehandler import StateEvaluator
from typing import Literal

class RouteHumanNode(StateEvaluator):
    def evaluate(self, state: StateGraph) -> Literal["end", "review"]:
        if len(state["messages"][-1].tool_calls) == 0:
            return "end"
        else:
            return "review"
