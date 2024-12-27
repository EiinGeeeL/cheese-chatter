from dataclasses import dataclass
from langgraph.graph import END, START
from langgraph.prebuilt import ToolNode
from cheese.services.llm_services import LLMServices
from cheese.components.runnables.cheeseagent import CheeseAgent
from cheese.components.edges.evaluators.route_human_node import RouteHumanNode
from cheese.components.nodes.enhancers.simple_invoke import SimpleInvoke
from cheese.components.nodes.commands.human_review_tool_call import HumanReviewToolCall
from cheese.components.tools.messagesvault_tool import MessagesVaultTool
from cheese.entity.edge import ConditionalEdge, SimpleEdge
from cheese.entity.node import SimpleNode, CommandNode
from cheese.utils.common import read_yaml
from cheese.constants import *

# TODO Here you can add another subgraphs as nodes

@dataclass(frozen=True)
class ConfigGraph:
    ## RUNNABLES BUILDERS
    CHEESE_AGENT = CheeseAgent(model=LLMServices.model,
                               tools=[MessagesVaultTool()])

    ## NODES
    config_nodes = read_yaml(CONFIG_NODES_FILE_PATH)

    _NODE_1 = SimpleNode(enhancer=SimpleInvoke(CHEESE_AGENT),
                         name=config_nodes['NODE_1']['name'])
        
    _NODE_2 = ToolNode(tools=CHEESE_AGENT.tools,
                       name=config_nodes['NODE_2']['name'])

    _NODE_3 = CommandNode(commander=HumanReviewToolCall(),
                         name=config_nodes['NODE_3']['name'])

    ## EDGES
    _EDGE_1 = SimpleEdge(node_source=START, 
                         node_path=_NODE_1.name)

    _EDGE_2 = SimpleEdge(node_source=_NODE_2.name,
                         node_path=_NODE_1.name) 

    
    _EDGE_4 = ConditionalEdge(evaluator=RouteHumanNode(),
                              map_dict={
                                  "end": END, # If last call `tools`, then end.
                                  "review": _NODE_3.name, # Human review in the loop.
                                  },
                              node_source=_NODE_1.name,
                              node_path=_NODE_3.name,)