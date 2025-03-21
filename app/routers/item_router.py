from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud import item_crud
from app.schemas.item_schema import NewTodoItem, UpdateTodoItem, ResponseTodoItem

router = APIRouter(
    prefix="/lists/{todo_list_id}/items",
    tags=["Todo項目"]
)

@router.get("/", response_model=list[ResponseTodoItem])
def get_todo_items(db: Session = Depends(get_db)):
    return item_crud.get_todo_items(db)

@router.get("/{todo_item_id}", response_model=ResponseTodoItem)
def get_todo_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    return item_crud.get_todo_item(db, todo_list_id, todo_item_id)

@router.post("/", response_model=ResponseTodoItem)
def post_todo_item(todo_list_id: int, todo_item: NewTodoItem, db: Session = Depends(get_db)):
    return item_crud.create_todo_item(db, todo_list_id, todo_item)

@router.put("/{todo_item_id}", response_model=ResponseTodoItem)
def put_todo_item(todo_list_id: int, todo_item_id: int, todo_item: UpdateTodoItem, db: Session = Depends(get_db)):
    return item_crud.update_todo_item(db, todo_list_id, todo_item_id, todo_item)

@router.delete("/{todo_item_id}")
def delete_todo_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    return item_crud.delete_todo_item(db, todo_list_id, todo_item_id)
