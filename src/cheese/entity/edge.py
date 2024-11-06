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
    def __init__(
            self, 
            node_source: Union[str, Literal["START","END"]], 
            node_path: Union[str, Literal["START","END"]]
        ):
        self.node_source = node_source
        self.node_path = node_path

    @abstractmethod
    def get(self) -> Union[Tuple[Any, Any], Tuple[Any, Any, Any]]:
        """
        Returns the argumentos to add simple edges or conditios
        """
        pass

class SimpleEdge(Edge):
    def get(self) -> Tuple[str, str]:
        """
        Returns a tuple with node source and node path.
        """
        return (self.node_source, self.node_path)

class ConditionalEdge(Edge):
    def __init__(
        self, 
        node_source: Union[str, Literal["START", "END"]], 
        node_path: Union[str, Literal["START", "END"]],
        callable: StateEvaluator,
        config: ConfigDataclass
    ):
        super().__init__(node_source, node_path)
        self.callable = callable
        self.config = config

    @abstractmethod
    def _configure_mapping_dict(self) -> Dict[str, Any]:
        """
        Define edges conditions between the source node and the path node.
        """
        pass
    
    def get(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:
        """
        Returns a tuple containing:
        - A string representing the source node
        - A function (any callable) to apply as conditional edge
        - A dictionary with conditions between the nodes
        """
        return (self.node_source, self.callable, self._configure_mapping_dict())

