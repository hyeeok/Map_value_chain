from typing import Dict, List, Union

from app.database import get_dev_db, get_mvc_db
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud
from .schemas import *

router = APIRouter(prefix="/overview")


@router.get(
    "",
    response_model=OverviewList,
    response_model_by_alias=False,
)
async def read_overview_list(
    category: str | None = None,
    keyword: str | None = None,
    limit: int = 50,
    page: int = 1,
    db: Session = Depends(get_dev_db),
):
    try:
        search_category = ""
        if category == "firmName":
            search_category = "firm"
        elif category == "bizrNo":
            search_category = "bizr_no"
        elif category == "jurirNo":
            search_category = "corp_cls"
        elif category == "stockCode":
            search_category = "stock_code"

        result, total_count = crud.get_overview_list(
            category=search_category, keyword=keyword, limit=limit, page=page, db=db
        )
        response = {"length": total_count, "data": result}
        return response
    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search", response_model=List[Dict[str, Union[int, str]]])
async def read_company_items_by_category(
    term: str = Query(..., description="Search term"),
    category: str = Query(
        ..., description="Search category: 'firm' or 'bizr_no' or 'jurir_no"
    ),
    db: Session = Depends(get_dev_db),
):
    items = crud.get_company_items_by_category(term=term, category=category, db=db)
    return items


# @router.get("/index", response_model=DepsList, response_model_by_alias=False)
# def read_deps(db: Session = Depends(get_db)):
#     result = crud.get_deps(db=db)
#     return {"length": len(result), "data": result}


@router.get(
    "/{corp_code}",
    response_model=OverviewDetail,
    response_model_by_alias=False,
)
async def read_overview_detail(corp_code: str, db: Session = Depends(get_mvc_db)):
    try:
        dart_corp_info = crud.get_dart_corp_info(corp_code=corp_code, db=db)
        if dart_corp_info == None:
            return HTTPException(status_code=404, detail="dart data not found")

        crno = dart_corp_info.jurir_no  # 법인등록번호
        openapi_outline = crud.get_openapi_outline(crno=crno, db=db)
        if openapi_outline == None:
            return HTTPException(
                status_code=404, detail="openapi outline data not found"
            )

        is_sm_corp = None
        if openapi_outline.smenpyn:
            if openapi_outline.smenpyn.lower() == "y":
                is_sm_corp = True
            elif openapi_outline.smenpyn.lower() == "n":
                is_sm_corp = False

        affiliate_result = crud.get_openapi_affiliate(crno=crno, db=db)
        affiliate_list = [{"corpName": affiliate[1]} for affiliate in affiliate_result]

        response = OverviewDetail(
            stock_name=dart_corp_info.stock_name,
            bizr_no=dart_corp_info.bizr_no,
            jurir_no=dart_corp_info.jurir_no,
            corp_name=dart_corp_info.corp_name,
            corp_name_eng=dart_corp_info.corp_name_eng,
            corp_name_history=None,
            est_dt=dart_corp_info.est_dt,
            kospi={
                "listDate": openapi_outline.enpxchglstgdt,
                "delistDate": openapi_outline.enpxchglstgaboldt,
            },
            kosdaq={
                "listDate": openapi_outline.enpkosdaqlstgdt,
                "delistDate": openapi_outline.enpkosdaqlstgaboldt,
            },
            konex={
                "listDate": openapi_outline.enpkrxlstgdt,
                "delistDate": openapi_outline.enpkrxlstgaboldt,
            },
            hm_url=dart_corp_info.hm_url,
            phn_no=dart_corp_info.phn_no,
            adres=dart_corp_info.adres,
            ceo_nm=dart_corp_info.ceo_nm,
            affiliate_list=affiliate_list,
            smenpyn=is_sm_corp,
            isVenture=None,
            sub_corp_num=None,
            shareholder_num=None,
            enpempecnt=openapi_outline.enpempecnt,
            enppn1avgslryamt=openapi_outline.enppn1avgslryamt,
            audtrptopnnctt=openapi_outline.audtrptopnnctt,
            acc_mt=dart_corp_info.acc_mt,
            issuerRate=None,
            enpmainbiznm=openapi_outline.enpmainbiznm,
            classList=[],
        )
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/{corp_code}", response_model=CompanyOverview)
# async def read_overview_detail(corp_code: str, db: Session = Depends(get_mvc_db)):
#     dart_corp_info_data = crud.get_dart_corp_info(corp_code=corp_code, db=db)
#     corp_cls = crud.get_corp_cls(corp_code=corp_code, db=db)

#     crno = dart_corp_info_data.jurir_no
#     openapi_outline_data = crud.get_openapi_outline_data(crno=crno, db=db)
#     openapi_affiliate_data = crud.get_openapi_affiliate_data(crno=crno, db=db)
#     affiliate_name_list = [
#         openapi_affiliate.afilcmpynm for openapi_affiliate in openapi_affiliate_data
#     ]

#     listing_date_data = crud.get_listing_date(crno=crno, corp_cls=corp_cls, db=db)

#     company_overview = CompanyOverview(
#         corp_name=dart_corp_info_data.corp_name,
#         bizr_no=dart_corp_info_data.bizr_no,
#         jurir_no=dart_corp_info_data.jurir_no,
#         corp_name_eng=dart_corp_info_data.corp_name_eng,
#         ceo_nm=dart_corp_info_data.ceo_nm,
#         est_dt=dart_corp_info_data.est_dt,
#         listing_date=listing_date_data,
#         phn_no=dart_corp_info_data.phn_no,
#         adres=dart_corp_info_data.adres,
#         hm_url=dart_corp_info_data.hm_url,
#         enppn1avgslryamt=openapi_outline_data.enppn1avgslryamt,
#         actnaudpnnm=openapi_outline_data.actnaudpnnm,
#         audtrptopnnctt=openapi_outline_data.audtrptopnnctt,
#         affiliate_name_list=affiliate_name_list,
#     )

#     return company_overview
