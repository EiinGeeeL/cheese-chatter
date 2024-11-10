from typing import Union, Literal, Dict
from cheese.entity.statehandler import StateEvaluator

class SimpleEdge():
    def __init__(
            self, 
            node_source: Union[str, Literal["START","END"]], 
            node_path: Union[str, Literal["START","END"]]
        ):
        self.node_source = node_source
        self.node_path = node_path

class ConditionalEdge(SimpleEdge):
    def __init__(
        self,
        node_source: Union[str, Literal["START", "END"]], 
        node_path: Union[str, Literal["START", "END"]],
        map_dict: Dict[str, Union[str, Literal["START", "END"]]],
        evaluator: StateEvaluator,
    ):
        super().__init__(node_source, node_path)
        self.evaluator = evaluator
        self.map_dict = map_dict