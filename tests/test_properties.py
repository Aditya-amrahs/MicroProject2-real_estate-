# tests/test_properties.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# -------------------- CREATE test--------------------
def test_create_property():
    response = client.post(
        "/properties/",
        json={
            "title": "Test Property",
            "description": "Test Desc",
            "price": 500000,
            "city": "Delhi",
            "agent_id": 1,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Property"
    assert "id" in data


# -------------------- LIST tests--------------------
def test_get_properties():
    response = client.get("/properties/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# -------------------- DETAILS tests--------------------
def test_get_property_by_id():
    response = client.get("/properties/1")

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert "agent" in data
    assert "images" in data


# -------------------- UPDATE test--------------------
def test_update_property():
    response = client.put("/properties/1", json={"price": 800000})

    assert response.status_code == 200
    assert response.json()["price"] == 800000


# -------------------- DELETE test--------------------
def test_delete_property():
    # create temp property first
    create_res = client.post(
        "/properties/",
        json={
            "title": "Delete Test",
            "description": "Temp",
            "price": 300000,
            "city": "Noida",
            "agent_id": 1,
        },
    )

    prop_id = create_res.json()["id"]

    delete_res = client.delete(f"/properties/{prop_id}")

    assert delete_res.status_code == 200
    assert delete_res.json()["message"] == "Property deleted successfully"


# -------------------- SEARCH tests--------------------
def test_search_property_by_city():
    response = client.get("/properties/search/", params={"city": "Delhi"})

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_property_price_range():
    response = client.get(
        "/properties/search/", params={"min_price": 400000, "max_price": 1000000}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
