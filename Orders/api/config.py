from pydantic import BaseSettings


class Settings(BaseSettings):
    database_host: str
    database_port: str = 5432
    database_username: str
    database_password: str
    database_db: str = 'orders'
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
