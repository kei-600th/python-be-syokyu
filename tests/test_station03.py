from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_echo():
    """Station03合格判定テストコード."""
    query_params = {
        "message": "Hello",
        "name": "TechTrain",
    }
    response = client.get("/echo", params=query_params)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Message": "Hello TechTrain!"}
