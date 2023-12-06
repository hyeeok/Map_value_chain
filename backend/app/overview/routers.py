from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_dev_db, get_mvc_db

from . import crud
from .schemas import *

router = APIRouter(prefix="/overview")


def map_corp_cls(corp_cls: str):
    mapping = {"y": "KOSPI", "k": "KOSDAQ", "n": "KONEX"}
    return mapping.get(corp_cls.lower(), "etc")


@router.get(
    "",
    response_model=OverviewList,
    response_model_by_alias=False,
)
async def read_overview_list(
    category: Optional[str] = Query(
        None, description="stockName, stockCode, bizrNo, jurirNo"
    ),
    keyword: Optional[str] = None,
    limit: int = 20,
    page: int = 1,
    db: Session = Depends(get_mvc_db),
):
    try:
        search_category = None
        if category:
            search_category = {
                "stockName": "stock_name",
                "bizrNo": "bizr_no",
                "jurirNo": "corp_cls",
                "stockCode": "stock_code",
            }.get(category)

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
        ...,
        description="Search category: 'firm' or 'bizr_no' or 'jurir_no' or 'stock_code'",
        # 아직 mvc db에는 jurir_no가 없음
    ),
    db: Session = Depends(get_dev_db),
):
    items = crud.get_company_items_by_category(term=term, category=category, db=db)
    return items


@router.get("/index", response_model=DepsList, response_model_by_alias=False)
def read_deps(db: Session = Depends(get_mvc_db)):
    result = crud.get_deps(db=db)
    return {"length": len(result), "data": result}


@router.get("/relations", summary="(temp) update corp code for relation db")
async def update_corp_code(
    mvc_db: Session = Depends(get_mvc_db), dev_db: Session = Depends(get_dev_db)
):
    try:
        results = crud.get_relations(db=dev_db)
        results = [row._asdict() for row in results]
        for item in results:
            corp_code = crud.get_corp_code_by_corp_name(item["corp_name"], db=mvc_db)
            vendor_corp_code = crud.get_corp_code_by_corp_name(
                item["vendor_corp_name"], db=mvc_db
            )
            if not corp_code or not vendor_corp_code:
                continue
            crud.patch_corp_code_by_corp_name(
                corp_code=corp_code[0],
                corp_name=item["corp_name"],
                vendor_corp_name=item["vendor_corp_name"],
                vendor_corp_code=vendor_corp_code[0],
                db=dev_db,
            )
            print(item["corp_name"])
        response = {"msg": "completed"}
        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


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
                corp_class = "KOSDAQ"
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
    "/{corp_code}/relations",
    response_model=OverviewRelationList,
    response_model_by_alias=False,
)
async def read_overview_relations(
    corp_code: str,
    db: Session = Depends(get_dev_db),
):
    try:
        result = []
        depth_one_list = crud.get_vendor_corp_list(
            corp_code=corp_code, vendor_class=None, db=db
        )
        depth_one_list = [row._asdict() for row in depth_one_list]

        def process_vendor_corp(vendor_class: str):
            for depth_one_item in depth_one_list:
                depth_one_corp_code = depth_one_item["vendor_corp_code"]
                depth_one_vendor_class = depth_one_item["vendor_class"]
                if depth_one_corp_code and depth_one_vendor_class == vendor_class:
                    depth_two_list = crud.get_vendor_corp_list(
                        corp_code=depth_one_corp_code,
                        vendor_class=vendor_class,
                        db=db,
                    )
                    depth_two_list = [row._asdict() for row in depth_two_list]
                    result.extend(depth_two_list)
                    result.append(depth_one_item)

        process_vendor_corp("구매")
        process_vendor_corp("판매")

        response = {"length": len(result), "data": result}
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
    # 테스트코드 = corp_code = '00100601'
    dart_corp_info = crud.get_dart_corp_info(corp_code=corp_code, db=db)
    if dart_corp_info is None:
        return HTTPException(
            status_code=404, detail="DART data not found for the given corp_code"
        )

    stcd = dart_corp_info.stock_code
    naver_stock_price = crud.get_naver_stock_price(stcd=stcd, db=db)
    krx_corp_info = crud.get_krx_corp_info(stcd=stcd, db=db)
    # dart_balance_sheet = crud.get_dart_balance_sheet(stcd=stcd, db=db)

    response = OverviewFinancials(
        close_price=naver_stock_price.close_price,
        list_shrs=krx_corp_info.list_shrs,
        parval=krx_corp_info.parval,
        # currency=dart_balance_sheet.currency,
        # thstrm_amount=dart_balance_sheet.thstrm_amount,
    )
    return response


@router.get(
    "/{corp_code}/relations",
    response_model=OverviewRelations,
    response_model_by_alias=False,
)
async def read_overview_relations(corp_code: str, db: Session = Depends(get_mvc_db)):
    overviw_relation = crud.get_overview_relations
    pass
