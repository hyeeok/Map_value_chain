from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Union

from app.database import get_db
from . import crud
from .schemas import mvc_fake_data_list, CompanyOverview, openapi_corp_affiliate

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


@router.get("/{corp_code}", response_model=CompanyOverview)
async def read_company_overview_info(corp_code: str, db: Session = Depends(get_db)):
    dart_corp_info_data = crud.get_dart_corp_info(corp_code=corp_code, db=db)
    corp_cls = crud.get_corp_cls(corp_code=corp_code, db=db)

    crno = dart_corp_info_data.jurir_no
    openapi_outline_data = crud.get_openapi_outline_data(crno=crno, db=db)
    openapi_affiliate_data = crud.get_openapi_affiliate_data(crno=crno, db=db)
    affiliate_name_list = [
        openapi_affiliate.afilcmpynm for openapi_affiliate in openapi_affiliate_data
    ]

    listing_date_data = crud.get_listing_date(crno=crno, corp_cls=corp_cls, db=db)

    company_overview = CompanyOverview(
        corp_name=dart_corp_info_data.corp_name,
        bizr_no=dart_corp_info_data.bizr_no,
        jurir_no=dart_corp_info_data.jurir_no,
        corp_name_eng=dart_corp_info_data.corp_name_eng,
        ceo_nm=dart_corp_info_data.ceo_nm,
        est_dt=dart_corp_info_data.est_dt,
        listing_date=listing_date_data,
        phn_no=dart_corp_info_data.phn_no,
        adres=dart_corp_info_data.adres,
        hm_url=dart_corp_info_data.hm_url,
        enppn1avgslryamt=openapi_outline_data.enppn1avgslryamt,
        actnaudpnnm=openapi_outline_data.actnaudpnnm,
        audtrptopnnctt=openapi_outline_data.audtrptopnnctt,
        affiliate_name_list=affiliate_name_list,
    )

    return company_overview
