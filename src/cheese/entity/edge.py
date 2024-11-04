from abc import ABC, abstractmethod
from typing import Tuple, Dict, Callable, Any
from langgraph.graph import StateGraph
from cheese.utils.type_vars import ConfigDataclass


class Edge(ABC):
    @abstractmethod
    def condition(self, state: StateGraph) -> str:
        """
        Returns a string as the result of the edge execution.
        """
        pass

class ConditionalEdge(ABC):
    node_source: str
    node_path: str
    callable: Edge.condition
    config: ConfigDataclass
    
    @abstractmethod
    def _configure_mapping_dict(self) -> dict:
        """
        Define edges conditions between the source node and the path node after the start node is called.
        """
        pass
    @abstractmethod
    def generate_conditional_edges(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:
        """
        Returns a tuple containing:
        - A string representing the source node
        - A function (any callable) to apply as conditional edge
        - A dictionary with conditions between the nodes
        """
        pass