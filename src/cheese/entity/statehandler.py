from abc import ABC, abstractmethod
from langgraph.graph import StateGraph
from cheese.entity.langrunnable import LangRunnable

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
            runnable: LangRunnable
        ):
        self.runnable = runnable
    @abstractmethod
    def enhance(self, state: StateGraph) -> dict[str, list]:
        """
        Returns state with modifications made by a LangRunnable.
        """
        pass
