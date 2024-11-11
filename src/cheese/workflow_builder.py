import logging
from IPython.display import Image, display
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from cheese.config.config_manager import BASIC_EDGES, BASIC_NODES
from cheese.entity.models.stategraph import AgentState
from cheese.pipeline.managers.edge_manager import EdgeManager
from cheese.pipeline.managers.node_manager import NodeManager

## Graph Configuration
class WorkflowBuilder:
    logger: logging.Logger = logging.getLogger(__name__.split('.')[-1])
    
    def __init__(self):
        self.workflow: StateGraph = StateGraph(AgentState)
        self.memory: MemoryError = MemorySaver()
        self.edge_manager: EdgeManager = EdgeManager()
        self.node_manager:NodeManager = NodeManager()
        
        self.logger.info("WorkFlowBuilder initialized")

    def compile(self) -> StateGraph:
        self._configure_workflow()
        return self.workflow.compile(checkpointer=self.memory)
    
    def display_graph(self, save: bool = False, filepath: str = "graph.png") -> Image:
        """
        Display the compiled graph or save as a PNG image.
        """
        img_data = self.workflow.compile().get_graph().draw_mermaid_png()

        if save:
            with open(filepath, "wb") as f:
                f.write(img_data)
        else:
            return display(Image(img_data))
        
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
    
    def _configure_nodes(self) -> None:
        """
        Fill the nodes.
        """
        self.node_manager.add_nodes(nodes=BASIC_NODES)

    def _configure_edges(self) -> None:
        """
        Fill the edges.
        """        
        self.edge_manager.add_edges(edges=BASIC_EDGES)

  



