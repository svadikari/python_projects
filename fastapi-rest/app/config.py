from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_username: str = "dummy"
    database_password: str = "dummy"


settings = Settings()
