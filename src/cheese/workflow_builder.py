from IPython.display import Image, display
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from cheese.entity.models.stategraph import AgentState
from cheese.entity.edge import SimpleEdge, ConditionalEdge
from cheese.pipeline.managers.edge_manager import EdgeManager
from cheese.pipeline.managers.node_manager import NodeManager
from cheese.entity.node import SimpleNode

# TODO MOVE TO CONFIG
from cheese.components.edges.evaluators.should_continue_evaluator import ShouldContinueEvaluator
from cheese.components.nodes.enhancers.simple_invoke_enhancer import SimpleInvokeEnhancer
from cheese.components.cheeseagent_runnable import CheeseAgent
from cheese.components.tools.evolution_tool import EvolutionTool


## Graph Configuration
class WorkflowBuilder:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        self.memory = MemorySaver()
        self.edge_manager = EdgeManager()
        self.node_manager = NodeManager()

    def _configure_nodes(self) -> None:
        """
        Fill and define the nodes.
        """
        node1 = SimpleNode(
            enhancer=SimpleInvokeEnhancer(CheeseAgent()),
            name="cheeseagent",
        )
        
        node2 = ToolNode(
            tools=[EvolutionTool()], 
            name="cheesetools" ,
        )


        # fill the node manager
        self.node_manager.add_nodes(nodes=[node1, node2])

    def _configure_edges(self) -> None:
        """
        Fill and define the edges.
        """
        # Start Edge
        edge1 = SimpleEdge(
            node_source=START, 
            node_path="cheeseagent"
        ) 
        # This means that after `tools` is called, `agent` node is called next.
        edge2 = SimpleEdge(
            node_source="cheesetools", 
            node_path="cheeseagent"
        ) 
        edge3 = ConditionalEdge(
            evaluator=ShouldContinueEvaluator(),
            map_dict={
                "continue": "cheesetools", # If `tools`, then we call the tool node.
                "end": END, # Otherwise we finish.
            },
            node_source="cheeseagent",
            node_path="cheesetools",
        )

        # fill the edge manager
        self.edge_manager.add_edges(edges=[edge1, edge2, edge3])

    def _configure_workflow(self) -> None:
        """
        Ensemble the graph workflow.
        """
        # Configure the nodes
        self._configure_nodes()
        [self.workflow.add_node(*config) for config in self.node_manager.configs_nodes()]

        # Configure the edges
        self._configure_edges()
        [self.workflow.add_edge(*config) for config in self.edge_manager.configs_edges()]
        [self.workflow.add_conditional_edges(*config) for config in self.edge_manager.configs_conditional_edges()]

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

