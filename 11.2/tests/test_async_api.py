import pytest


@pytest.mark.asyncio
async def test_create_user_async(async_client, faker):
    payload = {"username": faker.user_name(), "age": faker.random_int(min=19, max=70)}

    response = await async_client.post("/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert set(body.keys()) == {"id", "username", "age"}
    assert body["username"] == payload["username"]
    assert body["age"] == payload["age"]


@pytest.mark.asyncio
async def test_get_existing_user_async(async_client, faker):
    payload = {"username": faker.user_name(), "age": faker.random_int(min=19, max=70)}
    create_response = await async_client.post("/users", json=payload)
    user_id = create_response.json()["id"]

    response = await async_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == user_id
    assert body["username"] == payload["username"]


@pytest.mark.asyncio
async def test_get_non_existing_user_async(async_client):
    response = await async_client.get("/users/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


@pytest.mark.asyncio
async def test_delete_existing_user_async(async_client, faker):
    payload = {"username": faker.user_name(), "age": faker.random_int(min=19, max=70)}
    create_response = await async_client.post("/users", json=payload)
    user_id = create_response.json()["id"]

    response = await async_client.delete(f"/users/{user_id}")

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_same_user_twice_async(async_client, faker):
    payload = {"username": faker.user_name(), "age": faker.random_int(min=19, max=70)}
    create_response = await async_client.post("/users", json=payload)
    user_id = create_response.json()["id"]

    first_response = await async_client.delete(f"/users/{user_id}")
    second_response = await async_client.delete(f"/users/{user_id}")

    assert first_response.status_code == 204
    assert second_response.status_code == 404
    assert second_response.json()["detail"] == "User not found"
