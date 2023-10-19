from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from . import crud
from .models import *

router = APIRouter(prefix="/mvc")


@router.get(
    "/industries",
    # response_model=list[Industry],
    tags=["todo"],
    summary="get industry list",
)
def get_industry_list(db: Session = Depends(get_db)):
    result = crud.get_industries(db=db)
    return result
