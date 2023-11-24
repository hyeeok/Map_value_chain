from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_dev_db as get_db

from . import crud
from .models import *
from .schemas import *

router = APIRouter(prefix="/flowmap")


@router.get("", response_model=Flowmap)
def read_main_flowmap(db: Session = Depends(get_db)):
    try:
        result = crud.get_main_flowmap(db=db)
        if result == None:
            response = {"node": [], "edge": []}
            return response
        return result

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.put("")
def update_main_flowmap(
    new_data: FlowmapCreate,
    db: Session = Depends(get_db),
):
    try:
        result = crud.put_main_flowmap(new_data=new_data, db=db)
        message = "updated successfully" if result else "nothing updated"
        response = {"message": message, "flowmap_id": result}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/industry-classes",
    response_model=IndustryClassList,
    response_model_by_alias=False,
)
def read_industry_class_list(db: Session = Depends(get_db)):
    try:
        result = crud.get_industry_class_list(db=db)
        response = {"length": len(result), "data": result}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{industry_class_id}", response_model=Flowmap)
def read_flowmap(industry_class_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.get_flowmap(industry_class_id=industry_class_id, db=db)
        if result == None:
            response = {"node": [], "edge": []}
            return response
        return result

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{industry_class_id}")
def update_flowmap(
    industry_class_id: int,
    new_data: FlowmapCreate,
    db: Session = Depends(get_db),
):
    try:
        result = crud.put_flowmap(
            industry_class_id=industry_class_id, new_data=new_data, db=db
        )
        message = "updated successfully" if result else "nothing updated"
        response = {"message": message, "flowmap_id": result}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))
