from abc import ABC, abstractmethod
from cheese.entity.config_stategraph import AgentState


class ConditionalEdge(ABC):
    @abstractmethod
    def edge(self, state: AgentState) -> str:
        """
        Returns a string as the result of the edge execution.
        """
        pass
