from typing import Any, Callable, Dict, Tuple
from langgraph.graph import END
from cheese.entity.config_stategraph import AgentState
from cheese.entity.edge import ConditionalEdge

class ShouldContinueEdge(ConditionalEdge):
    def __init__ (self, config: Any):
        self.config = config
        self.node_source = config.node_source
        self.node_path = config.node_path

    def _execute(self, state: AgentState) -> str:
        messages = state["messages"]
        last_message = messages[-1]
        return "continue" if last_message.tool_calls else "end"
    
    def _configure_mapping_dict(self) -> dict:

        mapping_dict = {
            # If `tools`, then we call the tool node.
            "continue": self.node_path,
            # Otherwise we finish.
            "end": END,
            }
        
        return mapping_dict
        
    
    def generate_conditional_edges(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:

        return (self.node_source, self._execute, self._configure_mapping_dict())
    