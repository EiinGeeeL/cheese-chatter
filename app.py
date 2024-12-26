from langgraph.checkpoint.memory import MemorySaver
from cheese.workflow_builder import WorkflowBuilder
from cheese.config.config_graph import ConfigGraph
from cheese.entity.models.stategraph import SharedState
from cheese.entity.models.inputgraph import InputState
from cheese.entity.models.outputgraph import OutputState
from cheese.utils.common import read_yaml
from cheese.utils.logger import setup_logging
from cheese.constants import *

## Read the config.yaml
config = read_yaml(CONFIG_FILE_PATH)

## Setup logging Configuration
setup_logging(config)

## Workflow Configuration for the main graph
workflow_builder = WorkflowBuilder(
    config=ConfigGraph, 
    state_schema=SharedState, 
    input=InputState, 
    output=OutputState,
    checkpointer=MemorySaver(),
)
main_graph = workflow_builder.compile() # compile the graph
workflow_builder.display_graph(save=True, filepath="artifacts/cheese_graph.png") # update the graph artifact

## Workflow Configuration for subgraphs
# TODO add subgraphs