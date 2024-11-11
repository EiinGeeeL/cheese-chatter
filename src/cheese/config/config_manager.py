from dataclasses import dataclass
from langgraph.graph import END, START
from langgraph.prebuilt import ToolNode
from cheese.pipeline.services.llm_services import LLMServices
from cheese.components.cheeseagent_runnable import CheeseAgent
from cheese.components.edges.evaluators.should_continue_evaluator import ShouldContinueEvaluator
from cheese.components.nodes.enhancers.simple_invoke_enhancer import SimpleInvokeEnhancer
from cheese.components.tools.evolution_tool import EvolutionTool
from cheese.entity.edge import ConditionalEdge, SimpleEdge
from cheese.entity.node import SimpleNode
from cheese.entity.runnable_builder import RunnableBuilder

@dataclass(frozen=True)
class ConfigManager:
    ## RUNNABLES BUILDERS
    CHEESE_AGENT = CheeseAgent(model=LLMServices.model,
                               tools=[EvolutionTool()])

    ## NODES
    _NODE_1 = SimpleNode(enhancer= SimpleInvokeEnhancer(CHEESE_AGENT),
                         name = "cheeseagent")
        
    _NODE_2 = ToolNode(tools=CHEESE_AGENT.tools,
                       name="cheesetools")

    ## EDGES
    _EDGE_1 = SimpleEdge(node_source=START, 
                         node_path=_NODE_1.name)

    _EDGE_2 = SimpleEdge(node_source=_NODE_2.name,
                         node_path=_NODE_1.name) 

    _EDGE_3 = ConditionalEdge(evaluator=ShouldContinueEvaluator(),
                              map_dict={
                                  "continue": _NODE_2.name, # If `tools`, then we call the tool node.
                                  "end": END, # Otherwise we finish.
                                  },
                              node_source=_NODE_1.name,
                              node_path=_NODE_2.name)

    def get_nodes(self):
        """
        Returns a list of all nodes settled as constans in the configuration.
        """
        return [
            attr_value 
            for _, attr_value in self.__class__.__dict__.items() 
            if isinstance(attr_value, (SimpleNode, ToolNode))
        ]

    def get_edges(self):
        """
        Returns a list of all edges settled as constans in the configuration.
        """
        return [
            attr_value 
            for _, attr_value in self.__class__.__dict__.items() 
            if isinstance(attr_value, SimpleEdge)
        ]

    def get_runnable_builders(self):
        """
        Returns a list of all runnable builders settled as constans in the configuration.
        """
        return [
            attr_value 
            for _, attr_value in self.__class__.__dict__.items() 
            if isinstance(attr_value, RunnableBuilder)
        ]