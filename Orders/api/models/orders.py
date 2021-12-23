
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from ..database import Base


class OrderEntity(Base):
    __tablename__ = "orders"
    order_no = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    item_id = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_dttm = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_detail = relationship("UserEntity")

