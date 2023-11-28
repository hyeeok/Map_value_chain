from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from app.database import get_dev_db
from app.database import get_mvc_db


from . import crud
from .models import *
from .schemas import *

router = APIRouter(prefix="/flowmap")


@router.get("", response_model=FlowmapList)
def read_main_flowmap(db: Session = Depends(get_mvc_db)):
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
    db: Session = Depends(get_mvc_db),
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
    response_model_by_alias=False,
)
def read_industry_class_list(db: Session = Depends(get_mvc_db)):
    try:
        result = crud.get_industry_class_list(db=db)
        industry_class_list = [
            IndustryClasses(
                industryClassCode=item[0],
                industryClassName=item[1],
                industryClassId=item[2],
                domainId=item[3],
                domainName=item[4],
                domainCode=item[5],
            )
            for item in result
        ]

        response = {"length": len(industry_class_list), "data": industry_class_list}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{industry_class_id}", response_model=FlowmapBase)
def read_flowmap(industry_class_id: int, db: Session = Depends(get_mvc_db)):
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
    db: Session = Depends(get_mvc_db),
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
