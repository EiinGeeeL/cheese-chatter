from abc import ABC, abstractmethod
from langgraph.graph import StateGraph
from cheese.entity.runnable_builder import RunnableBuilder


class StateEvaluator(ABC):
    @abstractmethod
    def evaluate(self, state: StateGraph) -> str:
        """
        Returns a string as the result of the edge execution.
        """
        pass


class StateEnhancer(ABC): 
    def __init__(
            self,
            runnable_builder: RunnableBuilder
        ):
        self.runnable = runnable_builder.get()
        
    @abstractmethod
    def enhance(self, state: StateGraph) -> dict[str, list]:
        """
        Returns state with modifications made by a Runnable.
        """
        pass
