import logging
from langchain_core.prompts import (
    ChatPromptTemplate, 
    FewShotChatMessagePromptTemplate, 
    MessagesPlaceholder,
)
from langchain_core.runnables import Runnable
from cheese.config.cheeseagent.history_config import history_template
from cheese.config.cheeseagent.prompting_config import system_template
from cheese.entity.runnable_builder import RunnableBuilder
from cheese.config.config_manager import ConfigManager as CM

# TODO THIS TO SOLVE THE CIRCULAR IMPORT
from cheese.components.tools.evolution_tool import EvolutionTool


class CheeseAgent(RunnableBuilder):
    config: CM.CheeseAgentConfig = CM.CheeseAgentConfig
    logger: logging.Logger = logging.getLogger(__name__.split('.')[-1])

    def __init__ (self):
        self.model = self.config.model
        self.tools = [EvolutionTool()] # self.config.tools # TODO TO SOLVE
        self._chain = None

    def _configure_chain(self) -> Runnable:
        # TODO few_shot with differents tasks
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

        # Bind tools to the model
        model_with_tools = self.model.bind_tools(self.tools)

        # Create the chain
        chain = prompt_template | model_with_tools

        return chain