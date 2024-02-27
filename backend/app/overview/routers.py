import time
from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_dev_db, get_mvc_db

from . import crud
from .schemas import *

import redis
import json

import os

router = APIRouter(prefix="/overview")


class OverviewDescriptionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, OverviewDescription):
            return obj.dict()
        return super().default(obj)


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
        # 아직 mvc db에는 bizr_no가 없음
    ),
    db: Session = Depends(get_dev_db),
):
    items = crud.get_company_items_by_category(term=term, category=category, db=db)
    return items


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
        start_time_before_redis = time.time()  # 레디스 저장 전 시간 기록

        redis_client = redis.StrictRedis(
            host="0.0.0.0", port=6379, decode_responses=True
        )

        redis_key = f"corp_code:{corp_code}"
        cached_data = redis_client.get(redis_key)

        if cached_data:
            # 캐시된 데이터가 있다면 이를 파싱하여 딕셔너리로 변환하여 반환
            # 캐시된 데이터에서 키 매핑 수정
            end_time_before_redis = time.time()  # 레디스 저장 전 시간 기록
            execution_time_before_redis = (
                end_time_before_redis - start_time_before_redis
            )

            cached_dict = json.loads(cached_data)
            cached_dict = {
                "stock_name": cached_dict["stockName"],
                "stock_code": cached_dict["stockCode"],
                "bizr_no": cached_dict["bizrNo"],
                "jurir_no": cached_dict["jurirNo"],
                "corp_name": cached_dict["corpName"],
                "corp_name_eng": cached_dict["corpNameEng"],
                "corp_name_history": cached_dict["corpNameHistory"],
                "est_dt": cached_dict["establishDate"],
                "corp_cls": cached_dict["corpClass"],
                "list_date": cached_dict["listDate"],
                "delist_date": cached_dict["delistDate"],
                "hm_url": cached_dict["homepageUrl"],
                "phn_no": cached_dict["phoneNum"],
                "adress": cached_dict["adress"],
                "ceo_nm": cached_dict["ceoName"],
                "ceo_nm_history": cached_dict["ceoNameHistory"],
                "affiliate_list": cached_dict["affiliateList"],
                "smenpyn": cached_dict["isSMCorp"],
                "isVenture": cached_dict["isVenture"],
                "sub_corp_list": cached_dict["subCorpList"],
                "enpempecnt": cached_dict["employeeNum"],
                "enppn1avgslryamt": cached_dict["avgSalary"],
                "audtrptopnnctt": cached_dict["auditorReportOpinion"],
                "acc_mt": cached_dict["settleMonth"],
                "issuerRate": cached_dict["issuerRate"],
                "enpmainbiznm": cached_dict["mainBiz"],
                "classList": cached_dict["classList"],
            }

            # 레디스 저장 후 수행 시간 출력
            start_time_after_redis = time.time()
            execution_time_after_redis = start_time_after_redis - end_time_before_redis
            print(f"Redis 전환 후 실행 시간: {execution_time_after_redis} 초")

            return OverviewDescription(**cached_dict)

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
            Affiliate(corpName=affiliate[0], corpCode=affiliate[1])
            for affiliate in affiliate_result
        ]

        sub_corp_result = crud.get_openapi_sub_company_list(crno=crno, db=db)
        sub_corp_list = [SubCorp(corpName=sub_corp[0]) for sub_corp in sub_corp_result]

        ceo_name_history_result = crud.get_ceo_name_history_by_corp_code(
            corp_code=corp_code, db=db
        )
        ceo_name_history_list = [
            CeoNameHistory(
                seq=ceo_name_history[0],
                ceoName=ceo_name_history[1],
                update_date=ceo_name_history[2],
            )
            for ceo_name_history in ceo_name_history_result
        ]

        corp_name_history_result = crud.get_corp_name_history_by_corp_code(
            corp_code=corp_code, db=db
        )
        corp_name_history_list = [
            CorpNameHistory(
                seq=corp_name_history[0],
                corpName=corp_name_history[1],
                update_date=corp_name_history[2],
            )
            for corp_name_history in corp_name_history_result
        ]

        response = OverviewDescription(
            stock_name=dart_corp_info.stock_name,
            stock_code=dart_corp_info.stock_code,
            bizr_no=dart_corp_info.bizr_no,
            jurir_no=dart_corp_info.jurir_no,
            corp_name=dart_corp_info.corp_name,
            corp_name_eng=dart_corp_info.corp_name_eng,
            corp_name_history=corp_name_history_list,
            corp_cls=corp_class,
            est_dt=dart_corp_info.est_dt,
            list_date=list_date,
            delist_date=delist_date,
            hm_url=dart_corp_info.hm_url,
            phn_no=dart_corp_info.phn_no,
            adres=dart_corp_info.adres,
            ceo_nm=dart_corp_info.ceo_nm,
            ceo_nm_history=ceo_name_history_list,
            affiliate_list=affiliate_list,
            smenpyn=openapi_outline.smenpyn,
            isVenture=None,
            sub_corp_list=sub_corp_list,
            enpempecnt=openapi_outline.enpempecnt,
            enppn1avgslryamt=openapi_outline.enppn1avgslryamt,
            audtrptopnnctt=openapi_outline.audtrptopnnctt,
            acc_mt=dart_corp_info.acc_mt,
            issuerRate=None,
            enpmainbiznm=openapi_outline.enpmainbiznm,
            classList=[],
        )

        # 레디스에 데이터 저장
        redis_client.setex(
            redis_key,
            600,
            json.dumps(response, cls=OverviewDescriptionEncoder, ensure_ascii=False),
        )

        # 레디스에 저장하기 전 수행 시간 출력
        end_time_before_redis = time.time()
        execution_time_before_redis = end_time_before_redis - start_time_before_redis
        print(f"Redis 전환 전 실행 시간: {execution_time_before_redis} 초")

        return response

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{corp_code}/shareholders",
    response_model=OverviewShareholderList,
    response_model_by_alias=False,
)
async def read_overview_description_shareholders(
    corp_code: str, db: Session = Depends(get_mvc_db)
):
    try:
        shareholder_result = crud.get_shareholder_list_by_corp_code(
            corp_code=corp_code, db=db
        )
        shareholder_list = [
            Shareholder(
                nm=shareholder.nm,
                relate=shareholder.relate,
                stock_knd=shareholder.stock_knd,
                reprt_code=shareholder.reprt_code,
                bsis_posesn_stock_co=shareholder.bsis_posesn_stock_co,
                bsis_posesn_stock_qota_rt=shareholder.bsis_posesn_stock_qota_rt,
                trmend_posesn_stock_co=shareholder.trmend_posesn_stock_co,
                trmend_posesn_stock_qota_rt=shareholder.trmend_posesn_stock_qota_rt,
                rm=shareholder.rm,
            )
            for shareholder in shareholder_result
        ]
        response = {"length": len(shareholder_list), "data": shareholder_list}
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
    "/{isu_cd}/financials",
    response_model=OverviewFinancialList,
    response_model_by_alias=False,
)
async def read_overview_financials(isu_cd: str, db: Session = Depends(get_mvc_db)):
    # dart_corp_info = crud.get_dart_corp_info(corp_code=corp_code, db=db)
    # if dart_corp_info is None:
    #     return HTTPException(
    #         status_code=404, detail="DART data not found for the given corp_code"
    #     )

    # stcd = dart_corp_info.stock_code
    result = crud.get_mktcap_percent(isu_cd=isu_cd, db=db)
    response = {"data": result}
    return response
