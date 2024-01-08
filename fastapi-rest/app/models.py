from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    units = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))

    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product")
