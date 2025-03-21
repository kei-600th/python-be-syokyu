from sqlalchemy.orm import Session

from app.const import TodoItemStatusCode
from app.models.item_model import ItemModel
from app.models.list_model import ListModel
from app.schemas.item_schema import NewTodoItem, UpdateTodoItem

def get_todo_items(db: Session):
    return db.query(ItemModel).all()

def get_todo_item(db: Session, todo_list_id: int, todo_item_id: int):
    return db.query(ItemModel).filter(
        ItemModel.id == todo_item_id,
        ListModel.id == todo_list_id
    ).first()

def create_todo_item(db: Session, todo_list_id: int, todo_item: NewTodoItem):
    db_item = ItemModel(
        todo_list_id=todo_list_id,
        title=todo_item.title,
        description=todo_item.description,
        status_code=TodoItemStatusCode.NOT_COMPLETED.value,
        due_at=todo_item.due_at
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo_item(db: Session, todo_list_id: int, todo_item_id: int, todo_item: UpdateTodoItem):
    db_item = db.query(ItemModel).filter(
        ItemModel.id == todo_item_id,
        ListModel.id == todo_list_id
    ).first()
    db_item.title = todo_item.title
    db_item.description = todo_item.description
    db_item.status_code = TodoItemStatusCode.COMPLETED.value if todo_item.complete else TodoItemStatusCode.NOT_COMPLETED.value
    db_item.due_at = todo_item.due_at
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_todo_item(db: Session, todo_list_id: int, todo_item_id: int):
    db_item = db.query(ItemModel).filter(
        ItemModel.id == todo_item_id,
        ListModel.id == todo_list_id
    ).first()
    db.delete(db_item)
    db.commit()
    return {}
