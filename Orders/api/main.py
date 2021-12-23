from fastapi import FastAPI

from .database import engine
from .models import users as user_entity, orders as order_entity
from .routers import users, orders, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)


# Create Tables based on Entities
order_entity.Base.metadata.create_all(bind=engine)
user_entity.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World to Python FASTAPI Course!"}
