from typing import Union, Set, List, Type
from cheese.entity.edge import SimpleEdge, ConditionalEdge

class EdgeManager:
    def __init__(self):
        self.edges: set[Union[SimpleEdge, ConditionalEdge]] = set()

    def add_edges(self, edges: List[Union[SimpleEdge, ConditionalEdge]]) -> None:
        """
        Add one or more edges to the appropriate set based on their type.

        """

        for e in edges:
            if isinstance(e, (SimpleEdge, ConditionalEdge)):
                self.edges.add(e)
            else:
                raise TypeError("Each edge must be a SimpleEdge or ConditionalEdge")

    
    def get_edges(self, filter_type: Union[Type[SimpleEdge], Type[ConditionalEdge], None] = None) -> Union[Set[Union[SimpleEdge, ConditionalEdge]], Set[SimpleEdge], Set[ConditionalEdge]]:
        """
        Retrieve your edges, optionally filtered by type.
        """
        if filter_type is None:
            return self.edges
        elif issubclass(filter_type, (SimpleEdge, ConditionalEdge)):
            return {edge for edge in self.edges if isinstance(edge, filter_type)}
        else:
            raise TypeError("your filter type not identify")

