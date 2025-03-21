from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.models import list_model

client = TestClient(app)


def test_get_todo_list(db_session):
    """Station06合格判定テストコード."""
    db_item = list_model.ListModel(title="station06_test", description="A test record for station06.")

    # テスト用にインサート
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)

    # テスト実行
    response = client.get(f"/lists/{db_item.id}")

    # 実行結果の検証
    assert response.status_code == status.HTTP_200_OK

    response_body = response.json()
    assert response_body["id"] == db_item.id
    assert response_body["title"] == "station06_test"
    assert response_body["description"] == "A test record for station06."
    assert response_body["created_at"] == db_item.created_at.strftime("%Y-%m-%dT%H:%M:%S")
    assert response_body["updated_at"] == db_item.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
