from typing import Literal, Any
from langgraph.graph import StateGraph
from langgraph.types import Command, interrupt
from cheese.entity.node import StateCommander
from cheese.utils.common import read_yaml
from cheese.constants import *



class HumanReviewToolCall(StateCommander):
    config_nodes = read_yaml(CONFIG_NODES_FILE_PATH)
    
    @staticmethod
    def command(state: StateGraph(state_schema=Any)) -> Command[Literal[tuple(config_nodes['NODE_3']['route'].values())]]: # type: ignore
        last_message = state["messages"][-1]
        tool_call = last_message.tool_calls[-1]

        # this is the value we'll be providing via Command(resume=<human_review>)
        human_review = interrupt(
            {
                "question": "¿Estás seguro de eso?",
                # Surface tool calls for review
                "tool_call": tool_call,
            }
        )

        review_action = human_review["action"]
        review_data = human_review.get("data")

        # if approved, call the tool
        if review_action == "continue":
            return Command(goto=HumanReviewToolCall.config_nodes['NODE_3']['route']['tools'])

        # update the AI message AND call tools
        elif review_action == "update":
            updated_message = {
                "role": "ai",
                "content": last_message.content,
                "tool_calls": [
                    {
                        "id": tool_call["id"],
                        "name": tool_call["name"],
                        # This the update provided by the human
                        "args": review_data,
                    }
                ],
                # This is important - this needs to be the same as the message you replacing!
                # Otherwise, it will show up as a separate message
                "id": last_message.id,
            }
            return Command(goto=HumanReviewToolCall.config_nodes['NODE_3']['route']['tools'], update={"messages": [updated_message]})

        # provide feedback to LLM
        elif review_action == "feedback":
            # NOTE: we're adding feedback message as a ToolMessage
            # to preserve the correct order in the message history
            # (AI messages with tool calls need to be followed by tool call messages)
            tool_message = {
                "role": "tool",
                # This is our natural language feedback
                "content": review_data,
                "name": tool_call["name"],
                "tool_call_id": tool_call["id"],
            }
            return Command(goto=HumanReviewToolCall.config_nodes['NODE_3']['route']['enhancer'], update={"messages": [tool_message]})