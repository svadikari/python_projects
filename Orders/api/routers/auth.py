from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from api.database import get_db
from api.models.users import UserEntity
from api.schemas.user import Token, Login
from api.oauth2 import generate_jwt_token
from api.utils import verify_password

router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)


@router.post("", status_code=status.HTTP_200_OK, response_model=Token)
def login(user: Login, db: Session = Depends(get_db)):
    user_entity = db.query(UserEntity).filter(UserEntity.email == user.email).first()

    if not user_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    if not verify_password(user.password, user_entity.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid Credentials')
    return {"access_token": generate_jwt_token({"user_id": user_entity.id}), "token_type": "bearer"}
