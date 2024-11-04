from abc import ABC, abstractmethod
from typing import Tuple, Dict, Callable, Any, Union, Literal
from langgraph.graph import StateGraph
from cheese.utils.type_vars import ConfigDataclass


class StateEvaluator(ABC):
    @abstractmethod
    def condition(self, state: StateGraph) -> str:
        """
        Returns a string as the result of the edge execution.
        """
        pass

class Edge(ABC):
    node_source: Union[str, Literal["START", "END"]] # TODO str will be Node.id
    node_path: Union[str, Literal["START", "END"]] # TODO str will be Node.id

    @abstractmethod
    def get(self) -> Tuple[Any, Any]:
        """
        Returns a tuple with the node source and the node path
        """
        pass


class ConditionalEdge(Edge):
    callable: StateEvaluator.condition
    config: ConfigDataclass
    
    @abstractmethod
    def _configure_mapping_dict(self) -> dict:
        """
        Define edges conditions between the source node and the path node after the start node is called.
        """
        pass
    @abstractmethod
    def get(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:
        """
        Returns a tuple containing:
        - A string representing the source node
        - A function (any callable) to apply as conditional edge
        - A dictionary with conditions between the nodes
        """
        pass