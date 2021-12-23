from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.users import UserEntity
from ..schemas.user import UserResponse, TokenData, UserRequest
from ..oauth2 import get_current_user
from ..utils import hash_password

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post(path='', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def users(user: UserRequest, db: Session = Depends(get_db)):
    user.password = hash_password(user.password)
    new_user = UserEntity(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'{user.email} user already registered!')
    return new_user


@router.get(path='', status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def users(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    if current_user.role == 'admin':
        user_list = db.query(UserEntity).all()
    else:
        user_list = db.query(UserEntity).filter(UserEntity.id == current_user.user_id).all()
    if not user_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No User exists!')

    return user_list
