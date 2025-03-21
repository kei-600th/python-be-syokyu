"""定数定義モジュール."""

import os
from enum import Enum

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


class TodoItemStatusCode(Enum):
    """TODO項目のステータス."""
    NOT_COMPLETED = 1
    COMPLETED = 2
