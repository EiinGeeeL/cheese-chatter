from abc import ABC, abstractmethod
from typing import List, Any
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from cheese.utils.type_vars import LangModel


class LangRunnable(ABC):
    def __init__(
        self,
        model: LangModel,
        vectordb: Any, # TODO define class 
        tools: List[BaseTool],
    ):
        self.model = model
        self.vectordb: Any = vectordb
        self.tools = tools

        # Start the chain
        self._chain: Runnable = None

    @abstractmethod
    def _configure_chain(self) -> Runnable:
        """
        Configure the main chain and return it.
        """
        pass


    def invoke(self, message: str) -> str:
        """
        Invoke the chain.
        """
        if self._chain is None:
            self._chain = self._configure_chain()
        return self._chain.invoke(message)
        
    def get(self) -> Runnable:
        """
        Return the chain configured.
        """
        if self._chain is None:
            self._chain = self._configure_chain()
        return self._chain
    
