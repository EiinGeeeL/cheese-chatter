from langgraph.graph import END
from cheese.entity.edge import ConditionalEdge
from cheese.entity.dataclasses.conditional_edge_config import ShouldContinueConfig

class ShouldContinueConditionalEdge(ConditionalEdge):
    def __init__ (self):
        self.node_source = ShouldContinueConfig.node_source
        self.node_path = ShouldContinueConfig.node_path
        self.evaluator = ShouldContinueConfig.evaluator

    def _configure_mapping_dict(self) -> dict:
        mapping_dict = {
            "continue": self.node_path, # If `tools`, then we call the tool node.
            "end": END, # Otherwise we finish.
            }
        
        return mapping_dict