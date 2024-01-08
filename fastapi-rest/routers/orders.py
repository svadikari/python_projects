from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("", response_model=List[schemas.Order])
def orders(db: Session = Depends(database.get_db)):
    return db.query(models.Order).all()


@router.post("", response_model=schemas.Order)
def create_order(order: schemas.OrderBase, db: Session = Depends(database.get_db)):
    order_entity = models.Order()
    order_entity.units = order.units
    order_entity.product_id = order.product_id
    order_entity.customer_id = order.customer_id
    db.add(order_entity)
    db.commit()
    db.refresh(order_entity)

    return order_entity
