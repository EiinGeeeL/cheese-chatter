from typing import Tuple, Callable
from cheese.entity.statehandler import StateEnhancer
from cheese.entity.langrunnable import LangRunnable

class LangNode:
    def __init__(
        self, 
        id: str,
        enhancer: StateEnhancer,
        runnable: LangRunnable,
    ):
        self.id = id
        self.enhancer = enhancer
        self.runnable = runnable.get()

    def get_runnable(self) -> LangRunnable:
        return self.runnable

    def get(self) -> Tuple[str, Callable[..., StateEnhancer]]:
        return (self.id, self.enhancer.enhance)