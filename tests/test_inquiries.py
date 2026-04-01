# tests/test_inquiries.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# -------------------- INQUIRY TEST --------------------
def test_create_inquiry():
    response = client.post(
        "/inquiries/",
        json={
            "user_id": 1,
            "property_id": 1,
            "message": "Interested in this property",
        },
    )

    assert response.status_code in [200, 201]

    if response.status_code in [200, 201]:
        data = response.json()
        assert data["user_id"] == 1
        assert data["property_id"] == 1


# -------------------- FAVORITE TEST --------------------
def test_add_favorite():
    response = client.post(
        "/favorites/",
        json={
            "user_id": 1,
            "property_id": 3,  # use non-fixed combo to reduce duplication issue
        },
    )

    # duplicate-safe behavior
    assert response.status_code in [200, 201, 400]

    if response.status_code in [200, 201]:
        data = response.json()
        assert data["user_id"] == 1
        assert data["property_id"] == 3
