# from dataclasses import dataclass
# from abc import ABC, abstractmethod
# from typing import Tuple, Dict, Callable, Any
# from cheese.entity.config_stategraph import AgentState
# from langchain_core.messages import BaseMessage

# dataclass(frozen=True)
# class Node(ABC):
#     node_a: str
#     name_edge: str
#     node_b: str
#     # TODO nodes have to be a class because I can pass several nodes to conect, not just node a or node....
#     @abstractmethod
#     def _execute(self, state: AgentState) -> BaseMessage:
#         """
#         Abstract method to be implemented by subclasses.
#         Returns the action of the node.
#         """
#         pass
    
#     @abstractmethod
#     def generate_conditional_edges(self) -> Tuple[str, Callable[..., Any], Dict[str, Any]]:
#         """
#         Abstract method to be implemented by subclasses.
#         Returns a tuple containing:
#         - A string
#         - A function (any callable)
#         - A dictionary with string keys and any type of values
#         """
#         pass