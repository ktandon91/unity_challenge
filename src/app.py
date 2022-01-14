from fastapi import FastAPI
import uvicorn
from api.config import Config
from api.routes import games
from api.repository import db
app = FastAPI(title="Unity Challenge")

app.include_router(games.router, prefix='/api/games')


@app.on_event("startup")
async def startup():
    config = Config()
    await db.connect(path=config.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
