from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import Type

class CustomBaseTool:
    class MessagesVaultToolConfig:
        @dataclass
        class Input(BaseModel):
            """
            Input for the MessagesVaultTool
            """
            n_messages: int = Field(description="The number of the messages that the user want recover.")

        description: str = "This is a tool to give you the historical messages of a chat to make a summary when the user request a summary."
        args_schema: Type[BaseModel] = Input
        return_direct: bool = True

