from pydantic import BaseModel, Field

class InputChat(BaseModel):
    """Input for the chat endpoint."""

    messages: list = Field(
        ...,
        description="The human input to the model.",
    )