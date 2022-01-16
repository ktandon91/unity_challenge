from pydantic import BaseSettings

class Config(BaseSettings):
    app_name: str = "MongoDB API"
    db_path: str
    secret_key: str = "1213241241asasfafs"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    class Config:
        env_file = ".env"


settings = Config()
