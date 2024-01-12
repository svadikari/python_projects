from fastapi import Depends, status, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("", response_model=List[schemas.Product])
def products(db: Session = Depends(database.get_db)):
    return db.query(models.Product).all()


@router.get("/{product_id}", response_model=schemas.Product)
def products(product_id: int, db: Session = Depends(database.get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


@router.post("", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_products(product: schemas.ProductBase, db: Session = Depends(database.get_db)):
    product_entity = models.Product()
    product_entity.name = product.name
    product_entity.cost = product.cost
    db.add(product_entity)
    db.commit()
    db.refresh(product_entity)
    return product_entity

