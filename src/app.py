import os
import uvicorn

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from api.config import settings
from api.routes import auth, games, users
from api.repository import Repository, get_database, repo
from api.services import load_data as load_data_service


app = FastAPI(title="Unity Challenge")

app.include_router(auth.router)
app.include_router(games.router, prefix='/api/games')
app.include_router(users.router, prefix='/api/users')


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.get("/load")
async def load_sample_data(db: Repository = Depends(get_database)):
    await load_data_service.load_json_data(db)
    return {"message": "Sample data loaded successfully."}


@app.on_event("startup")
async def startup():
    db_url = os.getenv("DB_URL", settings.db_path)
    await repo.connect(url=db_url)


@app.on_event("shutdown")
async def shutdown():
    await repo.close()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
