import requests
import logging
from typing import Optional, Type
from langchain_core.tools import (
    BaseTool, 
    ToolException,
)
from langchain_core.callbacks import (
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel, SkipValidation
from cheese.entity.models.basetools import CustomBaseTool as CT



class MessagesVaultTool(BaseTool):
    # BaseTool atributes
    name: str = None
    description: str = None
    args_schema: Type[BaseModel] = None
    return_direct: bool = None

    # New BaseTool attributes
    config: SkipValidation[CT.MessagesVaultToolConfig] = CT.MessagesVaultToolConfig 
    logger: SkipValidation[logging.Logger] = logging.getLogger(__name__.split('.')[-1])
     
    def __init__(self, **data):
        super().__init__(**data)
        self.name = self.__class__.__name__
        self.description = self.config.description
        self.args_schema = self.config.args_schema
        self.return_direct = self.config.return_direct
        
        
    def _run(self, n_messages: int, run_manager: Optional[CallbackManagerForToolRun] = None) -> list[str]:
        """
        Run the tool logic
        """
        self.logger.info(f"Args: {n_messages}")

        url = f'http://192.168.1.224:8083/api/messages?size={n_messages}'
        response = requests.get(url)

        if response.status_code != 200:
            raise ToolException(f"Error: {n_messages} is not a valid argument")
        
        data = response.json()

        # Filter the id and timestand and reverse the messages
        parsed_data = [{k: v for k, v in item.items() if k != 'timestamp' and k != 'id'} for item in reversed(data)]


        return parsed_data