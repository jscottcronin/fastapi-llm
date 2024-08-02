"""FastAPI configuration settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NAME: str = "AWS Bedrock Demo App"
    VERSION: str = "0.3.0"
    DESCRIPTION: str = "A FastAPI application for invoking modern LLMs via AWS Bedrock."

    ANTHROPIC_CLUADE_3_HAIKU: str = "anthropic.claude-3-haiku-20240307-v1:0"
    ANTHROPIC_CLAUDE_3_SONNET: str = "anthropic.claude-3-sonnet-20240229-v1:0"


settings = Settings()

__all__ = ["settings"]
