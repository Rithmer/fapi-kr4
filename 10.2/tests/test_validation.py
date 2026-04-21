from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_payload() -> None:
    payload = {
        "username": "valid_user",
        "age": 24,
        "email": "valid@example.com",
        "password": "validpass",
    }

    response = client.post("/validate-user", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Payload accepted"


def test_invalid_payload_returns_custom_validation_error() -> None:
    payload = {
        "username": "invalid_user",
        "age": 18,
        "email": "invalid-email",
        "password": "123",
    }

    response = client.post("/validate-user", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert body["error"] == "Validation failed"
    assert body["code"] == 422
    assert len(body["details"]) >= 1
