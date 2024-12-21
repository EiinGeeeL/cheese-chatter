from typing import Literal
from langgraph.graph import StateGraph
from cheese.entity.statehandler import StateEvaluator

class ShouldContinue(StateEvaluator):
    def evaluate(self, state: StateGraph) -> Literal["end", "review"]:
        messages = state["messages"]
        last_message = messages[-1]
        return "continue" if last_message.tool_calls else "end"