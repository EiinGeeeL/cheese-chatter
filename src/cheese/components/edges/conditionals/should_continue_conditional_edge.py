from typing import Any, Callable, Dict, Tuple
from langgraph.graph import END
from cheese.entity.edge import ConditionalEdge
from cheese.entity.dataclasses.conditional_edge_config import ShouldContinueConfig

class ShouldContinueConditionalEdge(ConditionalEdge):
    def __init__ (self):
        self.config = ShouldContinueConfig()
        self.node_source = self.config.node_source
        self.node_path = self.config.node_path
        self.callable = self.config.callable

    def _configure_mapping_dict(self) -> dict:
        mapping_dict = {
            "continue": self.node_path, # If `tools`, then we call the tool node.
            "end": END, # Otherwise we finish.
            }
        
        return mapping_dict
        
    def get(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:
        return (self.node_source, self.callable, self._configure_mapping_dict())