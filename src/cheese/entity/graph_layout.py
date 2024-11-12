import logging
from langgraph.prebuilt import ToolNode
from dataclasses import is_dataclass
from typing import Annotated
from cheese.utils.type_vars import ConfigDataclass
from cheese.entity.edge import ConditionalEdge, SimpleEdge
from cheese.entity.node import SimpleNode
from cheese.entity.runnable_builder import RunnableBuilder

class GraphLayout:
    logger: logging.Logger = logging.getLogger(__name__.split('.')[-1])

    def __init__(self, config: Annotated[ConfigDataclass, is_dataclass]):
        """
        Initialize the Graph Layout with a dataclass instance containing configuration constants like edges and nodes.
        """
        if not is_dataclass(config):
            raise TypeError("Expected a dataclass type for the GraphLayout configuration.")
        else:
            self.config = config

        logging.info('GraphLayout initialized')
        
    def get_nodes(self):
        """
        Returns a list of all nodes defined in the configuration dataclass.
        """
        return [
            attr_value 
            for attr_value in self.config.__dict__.values() 
            if isinstance(attr_value, (SimpleNode, ToolNode))
        ]

    def get_edges(self):
        """
        Returns a list of all edges defined in the configuration dataclass.
        """
        return [
            attr_value 
            for attr_value in self.config.__dict__.values() 
            if isinstance(attr_value, (SimpleEdge, ConditionalEdge))
        ]

    def get_runnable_builders(self):
        """
        Returns a list of all runnable builders defined in the configuration dataclass.
        """
        return [
            attr_value 
            for attr_value in self.config.__dict__.values() 
            if isinstance(attr_value, RunnableBuilder)
        ]
