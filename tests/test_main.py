"""Unit tests for the main module."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200


def test_test():
    """Test the test endpoint."""
    response = client.get("/test")
    assert response.status_code == 200
