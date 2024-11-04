from cheese.components.edges.should_continue_edge import ShouldContinueEdge
from cheese.entity.edge import Edge
from dataclasses import dataclass

## ShouldContinueConfig
@dataclass(frozen=True)
class ShouldContinueConfig:
    node_source: str = 'cheeseagent'
    node_path: str = 'tools'
    callable: Edge.condition = ShouldContinueEdge().condition