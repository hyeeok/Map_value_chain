from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_dev_db
from app.database import get_mvc_db

from . import crud
from .schemas import *

router = APIRouter(prefix="/industry")


@router.get("", response_model=IndustryList, response_model_by_alias=False)
def read_industry_class(db: Session = Depends(get_dev_db)):
    try:
        result = crud.get_industry_class_list(db=db)
        return {"length": len(result), "data": result}

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/subclass", response_model=SubList, response_model_by_alias=False)
def read_sub_class(db: Session = Depends(get_dev_db)):
    try:
        result = crud.get_sub_class_list(db=db)
        return {"length": len(result), "data": result}

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))
