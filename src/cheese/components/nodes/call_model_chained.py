from cheese.components.main_model_chained import chain

def call_model_chained(state):
    messages = state["messages"]
    response = chain.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}