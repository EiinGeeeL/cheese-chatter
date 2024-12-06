from dataclasses import dataclass
from langgraph.graph import END, START
from langgraph.prebuilt import ToolNode
from cheese.services.llm_services import LLMServices
from cheese.components.runnables.cheeseagent import CheeseAgent
from cheese.components.edges.evaluators.should_continue_evaluator import ShouldContinueEvaluator
from cheese.components.nodes.enhancers.simple_invoke_enhancer import SimpleInvokeEnhancer
from cheese.components.tools.messagesvault_tool import MessagesVaultTool
from cheese.entity.edge import ConditionalEdge, SimpleEdge
from cheese.entity.node import SimpleNode

@dataclass(frozen=True)
class ConfigGraph:
    ## RUNNABLES BUILDERS
    CHEESE_AGENT = CheeseAgent(model=LLMServices.model,
                               tools=[MessagesVaultTool()])

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