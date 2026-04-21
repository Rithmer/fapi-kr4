from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_custom_exception_a() -> None:
    response = client.get("/exception-a")

    assert response.status_code == 418
    body = response.json()
    assert body["error"] == "CustomExceptionA was triggered"
    assert body["code"] == 418


def test_custom_exception_b() -> None:
    response = client.get("/exception-b/123")

    assert response.status_code == 404
    body = response.json()
    assert body["error"] == "CustomExceptionB: resource not found"
    assert body["code"] == 404
