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


@router.get("", response_model=FlowmapBase)
def read_flowmap(db: Session = Depends(get_db)):
    result = crud.get_flowmap(db=db)
    response = {"data": result}
    return response


@router.put("/{domainId}", response_model=FlowmapBase)
def update_flowmap(
    domainId: int, updated_data: FlowmapBase, db: Session = Depends(get_db)
):
    new_node = updated_data.data[0]
    new_edge = updated_data.data[1]
    print("44441898481kjashfjjsas1312" + new_edge, new_node)
    result = crud.set_flowmap(
        db=db, domainId=domainId, new_node=new_node, new_edge=new_edge
    )

    if not result:
        raise HTTPException(status_code=404, detail="Flowmap not found")

    return {"data": result}


@router.get("/{industryClassCode}", response_model=FlowmapBase)
def read_flowmap_industry(industryClassCode: int, db: Session = Depends(get_db)):
    result = crud.get_industry_class_flowmap(db=db, industryClassCode=industryClassCode)
    if not result:
        raise HTTPException(status_code=404, detail="Flowmap not found")
    response = {"data": result}
    return response
