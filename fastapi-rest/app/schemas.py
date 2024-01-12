from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class CustomerBase(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    email: EmailStr = Field(max_length=30)


class Customer(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime = None

    class Config:
        from_attributes: True


class ProductBase(BaseModel):
    name: str
    cost: float


class Product(BaseModel):
    id: int
    name: str
    cost: float
    created_at: datetime = None

    class Config:
        from_attributes: True


class OrderBase(BaseModel):
    units: int
    product_id: int
    customer_id: int


class Order(BaseModel):
    id: int
    units: int
    price: float = None
    product: Product = None
    customer: Customer = None
    created_at: datetime

    class Config:
        from_attributes = True


