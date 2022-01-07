from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, orders, auth

app = FastAPI(
    title="Orders",
    description="Order Place API",
    version="0.0.1",
    terms_of_service="https://github.com/svadikari/python_projects/tree/main/Orders/terms/",
    contact={
        "name": "Shyam Vadikari",
        "url": "http://shyam.com/contact/",
        "email": "svadikari@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)

origins = [
    "https://www.google.com",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Tables based on Entities using SQLAlchemy
# Disabling below metadata binding due to manual migration using alembic library
# order_entity.Base.metadata.create_all(bind=engine)
# user_entity.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World to Python FASTAPI Course!"}
