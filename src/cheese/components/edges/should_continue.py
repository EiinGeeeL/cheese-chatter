
def should_continue(state):
    """Determine whether to continue or end the conversation."""
    
    messages = state["messages"]
    last_message = messages[-1]
    return "continue" if last_message.tool_calls else "end"