from datetime import datetime

from pydantic import BaseModel

from api.schemas.user import UserResponse


class Order(BaseModel):
    item_id: str
    price: float


class OrderResponse(Order):
    order_no: str
    created_by: int
    created_dttm: datetime
    user_detail: UserResponse

    class Config:
        orm_mode = True
