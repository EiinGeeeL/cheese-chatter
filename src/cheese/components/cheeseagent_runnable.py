import logging
from typing import List
from langchain_core.prompts import (
    ChatPromptTemplate, 
    FewShotChatMessagePromptTemplate, 
    MessagesPlaceholder,
)
from cheese.config.cheeseagent.history_config import history_template
from cheese.config.cheeseagent.prompting_config import system_template
from cheese.entity.runnable_builder import RunnableBuilder
from cheese.pipeline.services.llm_services import LLMServices
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool


class CheeseAgent(RunnableBuilder):
    logger: logging.Logger = logging.getLogger(__name__.split('.')[-1])

    def __init__(self, model: LLMServices, tools: List[BaseTool]):
        super().__init__(model=model, vectordb=None, tools=tools)
    
        self.logger.info("CheeseAgent initialized")

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