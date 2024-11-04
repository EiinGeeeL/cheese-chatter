from IPython.display import Image, display
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from cheese.entity.models.stategraph import AgentState
from cheese.components.edges.conditionals.should_continue_conditional_edge import ShouldContinueConditionalEdge
from cheese.components.nodes.call_model_chained import call_model_chained
from cheese.components.main_model_chained import tools

## Graph Configuration
class WorkflowBuilder:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        # self.tools = tools # list # TODO define type
        self.memory = MemorySaver()
        self.tool_node = ToolNode(tools)
    
    # def _configure_toolnode(self):
    #     self.tool_node = ToolNode(self.tools)

    def _configure_workflow(self):
        """
        Ensemble the graph worflow.
        """
        # Define the nodes
        self.workflow.add_node("cheeseagent", call_model_chained)
        self.workflow.add_node("tools", self.tool_node)

        # Define the start edge
        self.workflow.add_edge(START, "cheeseagent")
    
        self.workflow.add_conditional_edges(*ShouldContinueConditionalEdge().get())

        # This means that after `tools` is called, `agent` node is called next.
        self.workflow.add_edge("tools", "cheeseagent")

    
    def compile(self):
        """
        Compiled the workflow into a graph.
        """
        # Finally, we compile it,
        # meaning you can use it as you would any other runnable
        self._configure_workflow()
        return self.workflow.compile(checkpointer=self.memory)
    

    def display_graph(self, save: bool = False, filepath: str = "graph.png"):
        """
        Display the compiled graph or save as a PNG image.
        """
        img_data = self.compile().get_graph().draw_mermaid_png()

        if save:
            with open(filepath, "wb") as f:
                f.write(img_data)
        else:
            return display(Image(img_data))

