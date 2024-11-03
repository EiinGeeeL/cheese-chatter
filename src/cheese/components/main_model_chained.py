from langchain_core.prompts import (
    ChatPromptTemplate, 
    FewShotChatMessagePromptTemplate, 
    MessagesPlaceholder,
)
from langchain_ollama import ChatOllama

from cheese.components.tools.evolution_tool import EvolutionTool
from cheese.utils.common import read_yaml
from cheese.constants import *
from cheese.config.config_history import history_template
from cheese.config.config_prompting import system_template
# %%
## Model Configuration
config = read_yaml(CONFIG_FILE_PATH)

# Initialize ChatOllama model
model = ChatOllama(
    model=config['ollama']['model'],
    temperature=config['ollama']['temperature'],
    # other params...
)

# %%
## Prompt Templates
# # This is a prompt template used to format each individual example.
# few_shot_map = ChatPromptTemplate.from_messages(
#     [
#         ("human", "{input}"),
#         ("ai", "{output}"),
#     ]
# )
# few_shot_prompt = FewShotChatMessagePromptTemplate(
#     example_prompt=few_shot_map,
#     examples=few_shot_template,
# )

# Create prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    # few_shot_prompt,
    history_template[0],
    MessagesPlaceholder(variable_name="messages"),
])

# %%
# Define tools
tools = [EvolutionTool()]

# Bind tools to the model
model_with_tools = model.bind_tools(tools)

# Create the chain
chain = prompt_template | model_with_tools
