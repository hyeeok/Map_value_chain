import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from . import crud
from .models import *
from .schemas import *

router = APIRouter(prefix="/flowmap")


@router.get("/industry-classes", response_model=IndustryClassList)
def read_industry_class_list(db: Session = Depends(get_db)):
    result = crud.get_industry_class_list(db=db)
    response = {"length": len(result), "data": result}
    return response


@router.get("", response_model=Flowmap)
def read_flowmap(db: Session = Depends(get_db)):
    result = crud.get_flowmap(db)
    return result


@router.put("", response_model=FlowmapBase)
def update_flowmap(new_data: FlowmapBase, db: Session = Depends(get_db)):
    result = crud.set_flowmap(db, new_data)
    return result