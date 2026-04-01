# tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)


def test_register_user():
    unique_email = f"user{int(time.time())}@test.com"
    response = client.post(
        "/register",
        params={
            "name": "Test User",
            "email": unique_email,
            "password": "test123",
        },
    )
    assert response.status_code in [200, 201]


def test_login_success():
    response = client.post(
        "/login", params={"email": "test@test.com", "password": "1234"}
    )

    assert response.status_code == 200
    assert "user_id" in response.json()


def test_login_invalid_password():
    response = client.post(
        "/login", params={"email": "test@test.com", "password": "wrongpass"}
    )

    assert response.status_code == 400


def test_login_nonexistent_user():
    response = client.post(
        "/login", params={"email": "nouser@example.com", "password": "pass123"}
    )

    assert response.status_code == 400
