"""FastAPI app for LLM requests."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Index Endpoint."""
    return {"message": "Hello World"}


@app.get("/health")
async def health() -> dict:
    """Health Check Endpoint."""
    return {"status": "ok"}


@app.get("/test")
async def test() -> dict:
    """Test endpoint."""
    return {"message": "test endpoint"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
