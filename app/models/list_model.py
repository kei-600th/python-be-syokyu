from typing import ClassVar

from sqlalchemy import Column, DateTime, Integer, String, func, text
from sqlalchemy.orm import relationship

from app.database import Base


class ListModel(Base):
    """TODOリストモデル."""

    __tablename__ = "todo_lists"
    __table_args__: ClassVar[dict[str]] = {
        "comment": "TODOリストテーブル",
    }

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(50), nullable=False)
    description = Column("description", String(200))
    created_at = Column("created_at", DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    items = relationship("ItemModel", backref="todo_lists")
