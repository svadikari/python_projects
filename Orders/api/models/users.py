from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
#from sqlalchemy.orm import relationship

from ..database import Base


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_dttm = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
   # orders = relationship("OrderEntity", back_populates="order_by")
