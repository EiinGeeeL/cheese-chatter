from fastapi import FastAPI
from langserve import add_routes

from cheese.entity.models.inputgraph import InputGraph
from cheese.workflow_builder import WorkflowBuilder
from cheese.config.config_graph import ConfigGraph
from cheese.utils.common import read_yaml
from cheese.utils.logger import setup_logging
from cheese.constants import *

## Read the config.yaml
config = read_yaml(CONFIG_FILE_PATH)

## Setup logging Configuration
setup_logging(config)

## FastAPI App Configuration
app = FastAPI(
    title=config['package']['repo_name'],
    version=config['package']['version'],
    description=config['package']['description'],
)

## Workflow Configuration
workflow_builder = WorkflowBuilder(config=ConfigGraph)
graph = workflow_builder.compile() # compile the graph
workflow_builder.display_graph(save=True, filepath="artifacts/cheese_graph.png")

add_routes(
    app,
    graph.with_types(input_type=InputGraph, output_type=dict), 
    path=f"/{config['package']['src_repo']}",
)
