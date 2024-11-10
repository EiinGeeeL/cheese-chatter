from cheese.entity.statehandler import StateEnhancer

class SimpleNode:
    def __init__(
        self,
        enhancer: StateEnhancer, 
        name: str,
        
    ):
        self.enhancer = enhancer
        self.name = name