import os

from fastapi import FastAPI

from app.routers import list_router, item_router

DEBUG = os.environ.get("DEBUG", "") == "true"

app = FastAPI(
    title="Python Backend Stations",
    debug=DEBUG,
)

if DEBUG:
    from debug_toolbar.middleware import DebugToolbarMiddleware

    # panelsに追加で表示するパネルを指定できる
    app.add_middleware(
        DebugToolbarMiddleware,
        panels=["app.database.SQLAlchemyPanel"],
    )

@app.get("/echo", tags=["Hello"])
def get_echo(message: str, name: str):
    return {"Message": f'{message} {name}!'}

@app.get("/health", tags=["System"])
def get_health():
    return {"status": "ok"}

app.include_router(list_router.router)
app.include_router(item_router.router)
