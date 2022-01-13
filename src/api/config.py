from pydantic import BaseSettings

class Config(BaseSettings):
    app_name: str = "MongoDB API"
    db_path: str

    class Config:
        env_file = ".env"
