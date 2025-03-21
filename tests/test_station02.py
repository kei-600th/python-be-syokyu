from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_hello():
    """Station02合格判定テストコード."""
    response = client.get("/hello")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Message": "Hello TechTrain!"}
