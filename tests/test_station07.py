from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.models import list_model

client = TestClient(app)


def test_post_todo_list(db_session) -> None:
    """Station07合格判定テストコード."""
    # テスト実行
    response = client.post("/lists", json={
        "title": "test_todo_station_07",
        "description": "This todo was made by the test of Station07.",
    })

    # 実行結果の検証
    assert response.status_code == status.HTTP_200_OK

    response_body = response.json()
    db_item = db_session.query(list_model.ListModel).filter(list_model.ListModel.id == response_body["id"]).first()

    if db_item is None:
        msg = "POSTしたデータがレスポンス情報に基づいて取得できませんでした。"
        raise AssertionError(msg)

    assert response_body["title"] == "test_todo_station_07"
    assert response_body["description"] == "This todo was made by the test of Station07."
    assert response_body["created_at"] == db_item.created_at.strftime("%Y-%m-%dT%H:%M:%S")
    assert response_body["updated_at"] == db_item.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
