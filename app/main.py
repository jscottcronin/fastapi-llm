"""FastAPI app for LLM requests."""

from anthropic.types.message import Message
from fastapi.responses import RedirectResponse

from app.core.app import create_app
from app.core.client import anthropic_client
from app.core.schemas import AnthropicBedrockRequest, AnthropicRequest

app = create_app()


@app.get("/")
async def root() -> RedirectResponse:
    """Index endpoint gets redirected to /docs."""
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health() -> dict:
    """Health Check Endpoint."""
    return {"status": "ok"}


@app.post("/anthropic")
async def anthropic(request: AnthropicRequest) -> Message:
    """Anthropic endpoint."""
    bedrock_request = AnthropicBedrockRequest.format(request)
    response = await anthropic_client.messages.create(**bedrock_request)
    return response
