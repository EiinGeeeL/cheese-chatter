from fastapi import FastAPI
from langserve import add_routes

from cheese.config.config_input import InputChat
from cheese.graph import graph
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

add_routes(
    app,
    graph.with_types(input_type=InputChat, output_type=dict), 
    path=f"/{config['package']['src_repo']}",
)
