from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_dev_db
from . import crud
from .schemas import *

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=str)
def login_user(user: User, db: Session = Depends(get_dev_db)):
    try:
        result = crud.login_user(user, db=db)
        if result:
            return f"id : {user.id} - 로그인 완료"
        else:
            return f"id : {user.id} - 로그인 실패"

    except Exception as e:
        print(repr(e))
        raise e


@router.post("/register", response_model=str)
def register_user(profile_info: ProfileInfo, db: Session = Depends(get_dev_db)):
    try:
        crud.register_user(profile_info, db=db)
        return f"id : {profile_info.id} - 회원가입 완료"

    except Exception as e:
        print(repr(e))
        raise e


@router.delete("/delete", response_model=str)
def delete_user(user: User, db: Session = Depends(get_dev_db)):
    try:
        result = crud.delete_user(user, db=db)
        if result:
            return f"id : {user.id} - 삭제 완료"
        else:
            return f"id : {user.id} - 삭제 실패"

    except Exception as e:
        print(repr(e))
        raise e
