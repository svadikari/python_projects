from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.orders import OrderEntity
from ..models.users import UserEntity
from ..oauth2 import get_current_user
from ..schemas.order import OrderResponse, Order
from ..schemas.user import TokenData

router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@router.post(path='', status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
def orders(order: Order, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    new_order = OrderEntity(created_by=current_user.user_id, **order.dict())
    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Couldn't save order")
    return new_order


@router.delete(path='/{order_no}', status_code=status.HTTP_200_OK)
def orders(order_no: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    order_query = db.query(OrderEntity).filter(OrderEntity.order_no == order_no)
    order = order_query.first()
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{order_no} order doesn't exists!")
    if order.order_by != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"You are not authorized to perform the operation!")
    order_query.delete(synchronize_session=False)
    db.commit()


@router.get(path='', status_code=status.HTTP_200_OK, response_model=List[OrderResponse])
def orders(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    if current_user.role == 'user':
        order_list = db.query(OrderEntity).filter(OrderEntity.created_by == current_user.user_id).all()
    else:
        order_list = db.query(OrderEntity).all()
    if not order_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No User exists!')
    return order_list
