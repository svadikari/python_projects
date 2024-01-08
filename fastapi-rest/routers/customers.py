from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("", response_model=List[schemas.Customer])
def customers(db: Session = Depends(database.get_db)):
    return db.query(models.Customer).all()


@router.post("", response_model=schemas.Customer)
def create_customers(customer: schemas.CustomerBase, db: Session = Depends(database.get_db)):
    customer_entity = models.Customer()
    customer_entity.name = customer.name
    customer_entity.email = customer.email
    db.add(customer_entity)
    db.commit()
    db.refresh(customer_entity)
    return customer_entity
