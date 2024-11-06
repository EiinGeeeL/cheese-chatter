from IPython.display import Image, display
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from cheese.entity.models.stategraph import AgentState
from cheese.entity.edge import SimpleEdge, ConditionalEdge
from cheese.pipeline.managers.edge_manager import EdgeManager
from cheese.components.edges.conditionals.should_continue_conditional_edge import ShouldContinueConditionalEdge
from cheese.components.nodes.call_model_chained import call_model_chained
from cheese.components.main_model_chained import tools

## Graph Configuration
class WorkflowBuilder:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        # self.tools = tools # list # TODO BASETOOL MANAGER
        self.memory = MemorySaver()
        self.tool_node = ToolNode(tools)
        self.edge_manager = EdgeManager()
        self.node_manager = None # TODO
    
    # def _configure_toolnode(self):
    #     self.tool_node = ToolNode(self.tools)


    def _configure_nodes(self) -> None:
        """
        Fill and define the nodes.
        """
        self.workflow.add_node("cheeseagent", call_model_chained)
        self.workflow.add_node("tools", self.tool_node)

    def _configure_edges(self) -> None:
        """
        Fill and define the edges.
        """
        edge1 = SimpleEdge(START, "cheeseagent") # Start edge
        edge2 = SimpleEdge("tools", "cheeseagent") # This means that after `tools` is called, `agent` node is called next.
        edge3 = ShouldContinueConditionalEdge() # ConditionalEdge

        # fill the edge manager
        self.edge_manager.add_edges(edges=[edge1, edge2, edge3])

    def _configure_workflow(self) -> None:
        """
        Ensemble the graph workflow.
        """
        # Configure the nodes
        self._configure_nodes()

        # Configure the edges
        self._configure_edges()
        [self.workflow.add_edge(*edge.get()) for edge in self.edge_manager.get_edges(filter_type=SimpleEdge)]
        [self.workflow.add_conditional_edges(*cond_edge.get()) for cond_edge in self.edge_manager.get_edges(filter_type=ConditionalEdge)]

    def compile(self) -> StateGraph:
        """
        Compiled the workflow into a graph.
        """
        self._configure_workflow()
        # Finally, we compile it to use it as runnable
        return self.workflow.compile(checkpointer=self.memory)
    

    def display_graph(self, save: bool = False, filepath: str = "graph.png") -> Image:
        """
        Display the compiled graph or save as a PNG image.
        """
        img_data = self.compile().get_graph().draw_mermaid_png()

        if save:
            with open(filepath, "wb") as f:
                f.write(img_data)
        else:
            return display(Image(img_data))

