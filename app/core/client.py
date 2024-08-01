"""Bedrock Client Instance."""

import json

import aioboto3
from anthropic import AsyncAnthropicBedrock


class BedrockClient:
    """Bedrock Client."""

    def __init__(self) -> None:
        """Bedrock attributes."""
        self.session = aioboto3.Session()
        self.client = None

    async def initialize(self) -> None:
        """Initialize Bedrock Client."""
        self.client = await self.session.client("bedrock-runtime").__aenter__()

    async def cleanup(self) -> None:
        """Cleanup Bedrock Client."""
        if self.client:
            await self.client.__aexit__(None, None, None)
        self.client = None

    async def invoke_model(self, body: dict, model_id: str) -> dict:
        """Invokes a model with the given body and model ID.

        Args:
            body (dict): The request body to send to Bedrock.
            model_id (str): The ID of the model to invoke in Bedrock.

        Returns:
            dict: The response from Bedrock.

        """
        if self.client:
            response = await self.client.invoke_model(body=body, modelId=model_id)
            response["body"] = json.loads((response["body"].read()).decode("utf-8"))
            return response

        raise (RuntimeError("Bedrock client not initialized."))


bedrock_client = BedrockClient()
anthropic_client = AsyncAnthropicBedrock()

__all__ = ["anthropic_client", "bedrock_client"]
