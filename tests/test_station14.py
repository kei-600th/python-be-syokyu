from importlib import import_module

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "import_path",
    [
        ("app.routers.item_router"),
        ("app.routers.list_router"),
        ("app.schemas.item_schema"),
        ("app.schemas.list_schema"),
        ("app.models.item_model"),
        ("app.models.list_model"),
        ("app.crud.item_crud"),
        ("app.crud.list_crud"),
    ],
)
def test_organize_project(import_path: str) -> None:
    """Station14合格判定テストコード.

    モジュールが意図した配置になっているかをテスト.
    """
    try:
        import_module(import_path)
    except ImportError as e:
        msg = f"{import_path}がImportできませんでした"
        raise AssertionError(msg) from e


def test_proper_endpoints_exist() -> None:
    """Station14合格判定テストコード.

    ルーティングの定義がデグレすることなく存在しているかをテスト.
    """
    response = client.get("/openapi.json")

    expected_endpoints = [
        "POST /lists/",
        "GET /lists/{todo_list_id}",
        "PUT /lists/{todo_list_id}",
        "DELETE /lists/{todo_list_id}",
        "POST /lists/{todo_list_id}/items/",
        "GET /lists/{todo_list_id}/items/{todo_item_id}",
        "PUT /lists/{todo_list_id}/items/{todo_item_id}",
        "DELETE /lists/{todo_list_id}/items/{todo_item_id}",
    ]

    open_api_schema = response.json()

    endpoints = []
    for api_path, detail in open_api_schema["paths"].items():
        for method in detail:
            endpoints.append(f"{method.upper()} {api_path}")  # noqa: PERF401

    for expected in expected_endpoints:
        if expected not in endpoints:
            msg = f"{expected}が存在しません。"
            raise AssertionError(msg)
