"""Application factory for FastAPI application."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.core.client import bedrock_client
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan context manager."""
    # Startup
    await bedrock_client.initialize()
    yield

    # Shutdown
    await bedrock_client.cleanup()


def create_app() -> FastAPI:
    """Create a FastAPI application."""
    return FastAPI(
        title=settings.NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        lifespan=lifespan,
    )
