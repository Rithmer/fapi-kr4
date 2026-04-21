import pytest
from faker import Faker
from httpx import ASGITransport, AsyncClient

from app.main import app, reset_memory_state


@pytest.fixture(autouse=True)
def clear_memory_db() -> None:
    reset_memory_state()
    yield
    reset_memory_state()


@pytest.fixture
async def async_client() -> AsyncClient:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def faker() -> Faker:
    return Faker()
