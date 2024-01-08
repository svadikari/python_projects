from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

SQL_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/orders-db"

engine = create_engine(SQL_URL)

SessionLocal = sessionmaker(autoflush=True, bind=engine, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

