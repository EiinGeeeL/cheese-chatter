from typing import Union, Tuple, List
from cheese.entity.edge import SimpleEdge, ConditionalEdge

class EdgeManager:
    def __init__(self):
        self.edges: set[SimpleEdge] = set()
        self.conditional_edges: set[ConditionalEdge] = set()

    def add_edges(self, edges: List[Union[SimpleEdge, ConditionalEdge]]) -> None:
        """
        Add one or more edges to the appropriate set based on their type.

        """

        for e in edges:
            if isinstance(e, SimpleEdge):
                self.edges.add(e)
            elif isinstance(e, ConditionalEdge):
                self.conditional_edges.add(e)
            else:
                raise TypeError("Each edge must be a SimpleEdge or ConditionalEdge")

    def get_edges(self) -> Tuple[set[SimpleEdge], set[ConditionalEdge]]:
        """
        Retrieve both sets of edges.

        Returns:
            Tuple[set[SimpleEdge], set[ConditionalEdge]]: A tuple containing two sets:
                - The set of regular edges
                - The set of conditional edges
        """
        return (self.edges, self.conditional_edges)
