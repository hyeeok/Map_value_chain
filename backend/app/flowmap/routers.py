from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import crud
from .models import *
from typing import List
from .schemas import *

router = APIRouter(prefix="/flowmap")


@router.get("/industry-classes", response_model=IndustryClassList)
def read_industry_class_list(db: Session = Depends(get_db)):
    result = crud.get_industry_class_list(db=db)
    response = {"length": len(result), "data": result}
    return response


@router.get("", response_model=Flowmap)
def read_flowmap(db: Session = Depends(get_db)):
    result = crud.get_flowmap(db=db)
    try:
        if result:
            response = {"node": result.node, "edge": result.edge}
            return response
        else:
            raise HTTPException(status_code=404)
    except:
        raise HTTPException(status_code=404)
