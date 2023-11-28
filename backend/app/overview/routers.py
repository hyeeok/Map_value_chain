from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_dev_db, get_mvc_db

from . import crud
from .schemas import *

router = APIRouter(prefix="/overview")


@router.get(
    "",
    response_model=OverviewList,
    response_model_by_alias=False,
)
async def read_overview_list(
    category: Optional[str] = Query(
        None, description="firmName, bizrNo, jurirNo, stockCode"
    ),
    keyword: Optional[str] | None = None,
    limit: int = 20,
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


@router.get("/index", response_model=DepsList, response_model_by_alias=False)
def read_deps(db: Session = Depends(get_mvc_db)):
    result = crud.get_deps(db=db)
    return {"length": len(result), "data": result}


@router.get(
    "/{corp_code}/description",
    response_model=OverviewDescription,
    response_model_by_alias=False,
)
async def read_overview_description(corp_code: str, db: Session = Depends(get_mvc_db)):
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

        corp_class, list_date, delist_date = None, None, None
        if dart_corp_info.corp_cls:
            if dart_corp_info.corp_cls.lower() == "y":
                corp_class = "KOSPI"  # kospi
                list_date = openapi_outline.enpxchglstgdt
                delist_date = openapi_outline.enpxchglstgaboldt
            elif dart_corp_info.corp_cls.lower() == "k":
                corp_class = "KODAQ"
                list_date = openapi_outline.enpkosdaqlstgdt
                delist_date = openapi_outline.enpkosdaqlstgaboldt
            elif dart_corp_info.corp_cls.lower() == "n":
                corp_class = "KONEX"
                list_date = openapi_outline.enpkrxlstgdt
                delist_date = openapi_outline.enpkrxlstgaboldt
            elif dart_corp_info.corp_cls.lower() == "e":
                corp_class = "etc"

        affiliate_result = crud.get_openapi_affiliate_list(crno=crno, db=db)
        affiliate_list = [
            Affiliate(corpName=affiliate[1]) for affiliate in affiliate_result
        ]

        sub_corp_result = crud.get_openapi_sub_company_list(crno=crno, db=db)
        sub_corp_list = [SubCorp(corpName=sub_corp[0]) for sub_corp in sub_corp_result]

        response = OverviewDescription(
            stock_name=dart_corp_info.stock_name,
            stock_code=dart_corp_info.stock_code,
            bizr_no=dart_corp_info.bizr_no,
            jurir_no=dart_corp_info.jurir_no,
            corp_name=dart_corp_info.corp_name,
            corp_name_eng=dart_corp_info.corp_name_eng,
            corp_name_history=None,
            corp_cls=corp_class,
            est_dt=dart_corp_info.est_dt,
            list_date=list_date,
            delist_date=delist_date,
            hm_url=dart_corp_info.hm_url,
            phn_no=dart_corp_info.phn_no,
            adres=dart_corp_info.adres,
            ceo_nm=dart_corp_info.ceo_nm,
            affiliate_list=affiliate_list,
            smenpyn=openapi_outline.smenpyn,
            isVenture=None,
            sub_corp_list=sub_corp_list,
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


@router.get(
    "/{corp_code}/financials",
    response_model=OverviewFinancials,
    response_model_by_alias=False,
)
async def read_overview_financials(corp_code: str, db: Session = Depends(get_mvc_db)):
    dart_corp_info = crud.get_dart_corp_info(corp_code=corp_code, db=db)
    if dart_corp_info is None:
        return HTTPException(
            status_code=404, detail="DART data not found for the given corp_code"
        )

    stcd = dart_corp_info.stock_code

    naver_stock_price = crud.get_naver_stock_price(stcd=stcd, db=db)
    print(naver_stock_price)
    if naver_stock_price is None:
        return HTTPException(
            status_code=404,
            detail="Naver stock price data not found for the given corp_code",
        )

    krx_corp_info = crud.get_krx_corp_info(stcd=stcd, db=db)
    if krx_corp_info is None:
        return HTTPException(
            status_code=404,
            detail="KRX corporate info not found for the given corp_code",
        )

    # dart_balance_sheet = crud.get_dart_balance_sheet(stcd=stcd, db=db)
    # if dart_balance_sheet is None:
    #     return HTTPException(
    #         status_code=404,
    #         detail="Dart balance sheet not found for the given corp_code",
    #     )

    response = OverviewFinancials(
        close_price=naver_stock_price.close_price,
        list_shrs=krx_corp_info.list_shrs,
        parval=krx_corp_info.parval,
        # currency=dart_balance_sheet.currency,
        # thstrm_amount=dart_balance_sheet.thstrm_amount,
    )
    return response
