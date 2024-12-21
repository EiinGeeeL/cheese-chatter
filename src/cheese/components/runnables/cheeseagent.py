import logging
from typing import List
from langchain_core.prompts import (
    ChatPromptTemplate, 
    FewShotChatMessagePromptTemplate, 
    MessagesPlaceholder,
)
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from cheese.config.runnables.cheeseagent.history_template import history_template
from cheese.config.runnables.cheeseagent.fewshot_examples import few_shot_examples
from cheese.config.runnables.cheeseagent.prompting_template import system_template
from cheese.entity.runnable_builder import RunnableBuilder
from cheese.services.llm_services import LLMServices
from cheese.utils.common import load_and_clean_text_file



class CheeseAgent(RunnableBuilder):
    logger: logging.Logger = logging.getLogger(__name__.split('.')[-1])

    def __init__(self, model: LLMServices, tools: List[BaseTool]):
        super().__init__(model=model, vectordb=None, tools=tools)
    
        self.logger.info("CheeseAgent initialized")

    def _configure_chain(self) -> Runnable:
        # Prepare the few_shot_prompt
        few_shot_map = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=few_shot_map,
            examples=few_shot_examples,
        )
        
        # Prepare the system_prompt
        context = load_and_clean_text_file('src/cheese/config/runnables/cheeseagent/prompt/contexto.txt')
        instructions = load_and_clean_text_file('src/cheese/config/runnables/cheeseagent/prompt/instrucciones.txt')
        input = load_and_clean_text_file('src/cheese/config/runnables/cheeseagent/prompt/input.txt')
        output_format = load_and_clean_text_file('src/cheese/config/runnables/cheeseagent/prompt/output_format.txt')
        restrictions = load_and_clean_text_file('src/cheese/config/runnables/cheeseagent/prompt/restricciones.txt')
        
        system_prompt = system_template.format(
            contexto=context,
            instrucciones=instructions,
            input=input,
            output_format=output_format,
            restricciones=restrictions
        )

        # Build the prompt template
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            few_shot_prompt,
            # history_template[0],
            MessagesPlaceholder(variable_name="messages"),
        ])

        # Bind tools to the model
        model_with_tools = self.model.bind_tools(self.tools)

        # Create the chain
        chain = prompt_template | model_with_tools

        return chain