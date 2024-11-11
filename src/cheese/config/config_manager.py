from typing import List
from langchain_core.tools import BaseTool

from cheese.pipeline.services.llm_services import LLMServices
from cheese.components.cheeseagent_runnable import CheeseAgent
from cheese.components.edges.evaluators.should_continue_evaluator import ShouldContinueEvaluator
from cheese.components.nodes.enhancers.simple_invoke_enhancer import SimpleInvokeEnhancer
from cheese.components.tools.evolution_tool import EvolutionTool
from cheese.entity.edge import ConditionalEdge, SimpleEdge
from langgraph.graph import END, START
from langgraph.prebuilt import ToolNode
from cheese.entity.node import SimpleNode

# class ConfigManager:
#     class CheeseAgentConfig:
#         model: LLMServices = LLMServices.model
#         tools: List[BaseTool] = [EvolutionTool()] # TODO The origin of the cirular import

CHEESE_AGENT = CheeseAgent(model = LLMServices.model,
                           tools = [EvolutionTool()] )

_ENHANCER = SimpleInvokeEnhancer(CHEESE_AGENT)

_NODE_1 = SimpleNode(
        enhancer= _ENHANCER,
        name = "cheeseagent",
    )
    
_NODE_2 = ToolNode(
    tools=CHEESE_AGENT.tools,
    name="cheesetools" ,
)

BASIC_NODES = [
    _NODE_1,
    _NODE_2
]

_EDGE_1 = SimpleEdge(
            node_source=START, 
            node_path=_NODE_1.name
        )

_EDGE_2 = SimpleEdge(
    node_source=_NODE_2.name,
    node_path=_NODE_1.name
) 

_EDGE_3 = ConditionalEdge(
    evaluator=ShouldContinueEvaluator(),
    map_dict={
        "continue": _NODE_2.name, # If `tools`, then we call the tool node.
        "end": END, # Otherwise we finish.
    },
    node_source=_NODE_1.name,
    node_path=_NODE_2.name,
)

BASIC_EDGES = [
    _EDGE_1, 
    _EDGE_2,
    _EDGE_3
]
