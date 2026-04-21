def test_create_user(client):
    payload = {"username": "alice", "age": 24}

    response = client.post("/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["username"] == payload["username"]
    assert body["age"] == payload["age"]


def test_get_existing_user(client):
    create_resp = client.post("/users", json={"username": "bob", "age": 30})
    user_id = create_resp.json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_get_non_existing_user(client):
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_delete_user(client):
    create_resp = client.post("/users", json={"username": "charlie", "age": 22})
    user_id = create_resp.json()["id"]

    response = client.delete(f"/users/{user_id}")

    assert response.status_code == 204


def test_delete_user_twice(client):
    create_resp = client.post("/users", json={"username": "diana", "age": 27})
    user_id = create_resp.json()["id"]

    first_response = client.delete(f"/users/{user_id}")
    second_response = client.delete(f"/users/{user_id}")

    assert first_response.status_code == 204
    assert second_response.status_code == 404
    assert second_response.json()["detail"] == "User not found"
