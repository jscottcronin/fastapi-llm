"""Pydantic schemas for Anthropic Requests."""

from typing import Literal

from pydantic import BaseModel, Field, field_validator

from app.core.settings import settings


class AnthropicMessage(BaseModel):
    """Anthropic message schema."""

    role: str
    content: str


class AnthropicRequest(BaseModel):
    """Anthropic request schema for FastAPI endpoint."""

    prompt: str
    model: Literal["haiku", "sonnet"] = Field("haiku", validate_default=True)
    max_tokens: int = Field(128, ge=1, le=4096)
    system: str | None = None
    temperature: float = Field(1.0, ge=0.0, le=1.0)
    start_sequence: str | None = None
    stop_sequences: list[str] | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prompt": "Tell me a fun fact.",
                    "model": "haiku",
                }
            ]
        }
    }

    @field_validator("model")
    @classmethod
    def validate_model(cls, v: str) -> str:
        """Convert model to model ID."""
        models = {
            "haiku": settings.ANTHROPIC_CLUADE_3_HAIKU,
            "sonnet": settings.ANTHROPIC_CLAUDE_3_SONNET,
        }
        return models[v]


class AnthropicBedrockRequest(BaseModel):
    """Anthropic request schema for AWS Bedrock."""

    model: str
    max_tokens: int
    messages: list[AnthropicMessage]
    system: str | None
    temperature: float
    stop_sequences: list[str] | None

    @classmethod
    def format(cls, request: AnthropicRequest) -> dict:
        """Convert Anthropic FastAPI Request to AnthropicBedrockRequest."""
        messages = [AnthropicMessage(role="user", content=request.prompt)]
        if request.start_sequence:
            messages.append(AnthropicMessage(role="assistant", content=request.start_sequence))

        return cls(
            model=request.model,
            max_tokens=request.max_tokens,
            messages=messages,
            system=request.system,
            temperature=request.temperature,
            stop_sequences=request.stop_sequences,
        ).model_dump(exclude_none=True)
