from sqlalchemy.orm import Session

from app.models.list_model import ListModel
from app.schemas.list_schema import NewTodoList, UpdateTodoList

def get_todo_lists(db: Session):
    return db.query(ListModel).all()

def get_todo_list(db: Session, todo_list_id: int):
    return db.query(ListModel).filter(ListModel.id == todo_list_id).first()

def create_todo_list(db: Session, todo_list: NewTodoList):
    db_item = ListModel(
        title=todo_list.title,
        description=todo_list.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo_list(db: Session, todo_list_id: int, todo_list: UpdateTodoList):
    db_item = db.query(ListModel).filter(ListModel.id == todo_list_id).first()
    db_item.title = todo_list.title
    db_item.description = todo_list.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_todo_list(db: Session, todo_list_id: int):
    db_item = db.query(ListModel).filter(ListModel.id == todo_list_id).first()
    db.delete(db_item)
    db.commit()
    return {}
