from typing import Set, List, Tuple, Union
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import Runnable
from cheese.entity.node import SimpleNode
from cheese.entity.statehandler import StateEnhancer

class NodeManager:
    def __init__(self):
        self.nodes: Set[Union[SimpleNode, ToolNode]] = set()

    def add_nodes(self, nodes: Union[SimpleNode, ToolNode, List[Union[SimpleNode, ToolNode]]]) -> None:
        """
        Add one or more SimpleNode or ToolNode instances to the set.
        """
        if not isinstance(nodes, list):
            nodes = [nodes]

        for node in nodes:
            if isinstance(node, (SimpleNode, ToolNode)):
                self.nodes.add(node)
            else:
                raise TypeError(f"Each node must be a SimpleNode or ToolNode, got {type(node)}")

    def get_nodes(self) -> Set[Union[SimpleNode, ToolNode]]:
        """
        Retrieve a set containing all added nodes.
        """
        return self.nodes

    def configs_nodes(self) -> Tuple[Tuple[str, Union[StateEnhancer.enhance, ToolNode]]]:
        """
        Retrieve a node configuration for StateGraph.
        """
        return ((node.name, node if isinstance(node, ToolNode) else node.enhancer.enhance) 
                for node in self.nodes)

    def remove_node(self, node: Union[SimpleNode, ToolNode]) -> None:
        """
        Remove a specific node from the set.
        """
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            raise ValueError("Node not found in the set")