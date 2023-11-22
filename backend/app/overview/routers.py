from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Union

from app.database import get_db
from . import crud
from .schemas import mvc_fake_data_list, CompanyDetailResponse

router = APIRouter(prefix="/overview")


@router.get("", response_model=mvc_fake_data_list)
async def read_company_overview(
    term: str = Query(..., description="Search term"),
    category: str = Query(
        ..., description="Search category: 'firm' or 'bizr_no' or 'jurir_no'"
    ),
    db: Session = Depends(get_db),
):
    result = crud.get_company_overview(term=term, category=category, db=db)
    return {"length": len(result), "data": result}


@router.get("/search", response_model=List[Dict[str, Union[int, str]]])
async def read_company_items_by_category(
    term: str = Query(..., description="Search term"),
    category: str = Query(
        ..., description="Search category: 'firm' or 'bizr_no' or 'jurir_no"
    ),
    db: Session = Depends(get_db),
):
    items = crud.get_company_items_by_category(term=term, category=category, db=db)
    return items


# @router.get("/index", response_model=DepsList, response_model_by_alias=False)
# def read_deps(db: Session = Depends(get_db)):
#     result = crud.get_deps(db=db)
#     return {"length": len(result), "data": result}


@router.get("/{corp_code}")
async def read_company_overview_info(corp_code: str, db: Session = Depends(get_db)):
    dart_corp_info_data = crud.get_dart_corp_info(corp_code=corp_code, db=db)
    crno = dart_corp_info_data.jurir_no
    print(crno)
    openapi_outline_data = crud.get_openapi_outline_data(crno=crno, db=db)
    openapi_affiliate_data = crud.get_openapi_affiliate_data(crno=crno, db=db)

    result = CompanyDetailResponse(
        dart_corp_info_data=dart_corp_info_data,
        openapi_outline_data=openapi_outline_data,
        openapi_affiliate_data=openapi_affiliate_data,
    )

    return result
