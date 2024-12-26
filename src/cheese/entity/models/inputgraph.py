from dataclasses import dataclass
from pydantic import BaseModel, Field


@dataclass
class InputState(BaseModel):
    """Input for the chat endpoint that start the graph workflow."""
    messages: list = Field(
        ...,
        description="The human input to the model.",
    )
