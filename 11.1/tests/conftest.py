import pytest
from fastapi.testclient import TestClient

from app.main import app, reset_memory_state


@pytest.fixture(autouse=True)
def clear_memory_db() -> None:
    reset_memory_state()
    yield
    reset_memory_state()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
