from fastapi.testclient import TestClient
from beerlog.api import api

client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers",
        json={
            "name": "Test",
            "style": "Testing",
            "flavor": 1,
            "image": 5,
            "cost": 8,
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Test"
    assert result["id"] == 1
