from fastapi import FastAPI

from api.config import Config
from api.repository import db
from api.routes import games

app = FastAPI(title="Async FastAPI")

app.include_router(games.router, prefix='/api/games')


@app.on_event("startup")
async def startup():
    config = Config()
    await db.connect(path=config.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close()

