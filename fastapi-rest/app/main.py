
from fastapi import FastAPI

from .database import engine
from . import models
from routers import orders, customers, products

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(orders.router)
app.include_router(customers.router)
app.include_router(products.router)
