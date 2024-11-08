from langgraph.graph import StateGraph
from cheese.entity.statehandler import StateEnhancer

class SimpleInvokeEnhancer(StateEnhancer):
    def enhance(self, state: StateGraph):
        messages = state["messages"]
        response = self.runnable.invoke(messages)
        # We return a list, because this will get added to the existing list
        return {"messages": [response]}