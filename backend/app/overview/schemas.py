from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel, Field, Json


class DepsBase(BaseModel):
    subClassId: Optional[int] = Field(..., alias="subclassid")
    subClassName: Optional[str] = Field(..., alias="subclassname")
    subClassCode: Optional[str] = Field(..., alias="subclasscode")
    subClassLevel: Optional[int] = Field(..., alias="subclasslevel")

    class Config:
        from_attributes = True


class Deps(DepsBase):
    domainId: Optional[int] = Field(..., alias="domainid")
    domainCode: Optional[str] = Field(..., alias="domaincode")
    domainName: Optional[str] = Field(..., alias="domainname")
    industryClassId: Optional[int] = Field(..., alias="industryclassid")
    industryClassName: Optional[str] = Field(..., alias="industryclassname")
    industryClassCode: Optional[str] = Field(..., alias="industryclasscode")

    class Config:
        from_attributes = True


class DepsList(BaseModel):
    length: int
    data: List[Deps]

    class Config:
        from_attributes = True


class OverviewBase(BaseModel):
    corpCode: str = Field(..., alias="corp_code")
    firmName: str = Field(..., alias="firm")
    bizrNo: str = Field(..., alias="bizr_no")
    jurirNo: str = Field(..., alias="corp_cls")
    stockCode: str = Field(..., alias="stock_code")
    conglomerateName: str | None = Field(None, alias="stock_name")
    ceoName: str | None = Field(None, alias="ceo_nm")
    establishDate: str = Field(..., alias="bsns_year")
    adress1: str = Field(..., alias="adres_1")
    adress2: str = Field(..., alias="adres_2")
    hompageUrl: str | None = Field(None, alias="hm_url")

    class Config:
        from_attributes = True


class OverviewList(BaseModel):
    length: int
    data: List[OverviewBase]


class dart_corp_info(BaseModel):
    corp_name: str = Field(..., alias="corp_name")
    bizr_no: str = Field(..., alias="bizr_no")
    jurir_no: str = Field(..., alias="jurir_no")
    corp_name_eng: str = Field(..., alias="corp_name_eng")
    ceo_nm: str = Field(..., alias="ceo_nm")
    est_dt: str = Field(..., alias="est_dt")
    phn_no: str = Field(..., alias="phn_no")
    adres: str = Field(..., alias="adres")
    hm_url: Optional[str] = Field(None, alias="hm_url")

    class Config:
        from_attributes = True


class openapi_corp_outline(BaseModel):
    enppn1avgslryamt: str = Field(None, alias="enppn1avgslryamt")
    actnaudpnnm: str = Field(None, alias="actnaudpnnm")
    audtrptopnnctt: str = Field(None, alias="audtrptopnnctt")

    class Config:
        from_attributes = True


class openapi_corp_affiliate(BaseModel):
    afilcmpynm: Optional[str] = Field(None, alias="afilcmpynm")

    class Config:
        from_attributes = True


class openapi_corp_affilate_list(openapi_corp_affiliate):
    affiliate_name_list: List[openapi_corp_affiliate]

    class Config:
        from_attributes = True


class CompanyOverview(openapi_corp_affilate_list, openapi_corp_outline, dart_corp_info):
    # 상장일 : 법인 구분에 따라 상장일자 맞춰서 표시 -> enpxchglstgdt(KOSPI), enpkosdaqlstgdt(KOSDAQ), enpkrxlstgdt(KONEX)
    # 지역 : 국가,지역대,지역소 필요
    # 관련계열사명 : 리스트로 가져와야함 -> openapi_corp_affilate_list
    # 중소기업, 벤처기업, 종속회사수, 주주수, 기업종업원수 여부 아직 없음
    pass
