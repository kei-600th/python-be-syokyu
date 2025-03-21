from fastapi.testclient import TestClient
from sqlalchemy import inspect

from app.database import engine
from app.main import app

client = TestClient(app)


def test_tables():
    """Station05合格判定テストコード."""
    inspector = inspect(engine)

    target_table_names = ["todo_lists", "todo_items"]
    existed_table = [table_name for table_name in inspector.get_table_names() if table_name in target_table_names]

    assert sorted(target_table_names) == sorted(existed_table)
