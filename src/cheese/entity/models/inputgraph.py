from pydantic import BaseModel, Field

## InputChat of the graph and app
class InputGraph(BaseModel):
    """Input for the chat endpoint."""

    messages: list = Field(
        ...,
        description="The human input to the model.",
    )