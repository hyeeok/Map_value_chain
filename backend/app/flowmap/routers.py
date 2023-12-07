from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_dev_db
from app.database import get_mvc_db
from app.flowmap.utils.generate_operations import generate_source_data


from . import crud
from .schemas import *

router = APIRouter(prefix="/flowmap")


@router.get("", response_model=FlowmapList)
def read_main_flowmap(
    mvc_db: Session = Depends(get_mvc_db), dev_db: Session = Depends(get_dev_db)
):
    try:
        result = crud.get_main_flowmap(db=mvc_db)
        # result = []
        if not result:
            industry_class_result = crud.get_industry_class_list(db=dev_db)
            industry_class_list = [item._asdict() for item in industry_class_result]
            node_list = generate_source_data(industry_class_list)
            response = {"node": node_list, "edge": []}
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
    response_model=IndustryClassList,
    response_model_by_alias=False,
)
def read_industry_class_list(db: Session = Depends(get_dev_db)):
    try:
        result = crud.get_industry_class_list(db=db)
        response = {"length": len(result), "data": result}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/{industry_class_id}", response_model=FlowmapBase)
# def read_flowmap(industry_class_id: int, db: Session = Depends(get_mvc_db)):
#     try:
#         result = crud.get_flowmap(industry_class_id=industry_class_id, db=db)
#         if result == None:
#             response = {"node": [], "edge": []}
#             return response
#         return result

#     except Exception as e:
#         print(repr(e))
#         raise HTTPException(status_code=500, detail=str(e))


# @router.put("/{industry_class_id}")
# def update_flowmap(
#     industry_class_id: int,
#     new_data: FlowmapCreate,
#     db: Session = Depends(get_mvc_db),
# ):
#     try:
#         result = crud.put_flowmap(
#             industry_class_id=industry_class_id, new_data=new_data, db=db
#         )
#         message = "updated successfully" if result else "nothing updated"
#         response = {"message": message, "flowmap_id": result}
#         return response

#     except Exception as e:
#         print(repr(e))
#         raise HTTPException(status_code=500, detail=str(e))
