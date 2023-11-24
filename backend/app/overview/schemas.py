from typing import List, Optional, TypedDict

from pydantic import BaseModel, Field
from typing_extensions import TypedDict


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


# class dart_corp_info(BaseModel):
#     corp_name: str = Field(..., alias="corp_name")
#     bizr_no: str = Field(..., alias="bizr_no")
#     jurir_no: str = Field(..., alias="jurir_no")
#     corp_name_eng: str = Field(..., alias="corp_name_eng")
#     ceo_nm: str = Field(..., alias="ceo_nm")
#     est_dt: str = Field(..., alias="est_dt")
#     listing_date: str
#     phn_no: str = Field(..., alias="phn_no")
#     adres: str = Field(..., alias="adres")
#     hm_url: Optional[str] = Field(None, alias="hm_url")

#     class Config:
#         from_attributes = True


# class openapi_corp_outline(BaseModel):
#     enppn1avgslryamt: str = Field(None, alias="enppn1avgslryamt")
#     actnaudpnnm: str = Field(None, alias="actnaudpnnm")
#     audtrptopnnctt: str = Field(None, alias="audtrptopnnctt")

#     class Config:
#         from_attributes = True


# class openapi_corp_affiliate(BaseModel):
#     afilcmpynm: str = Field(None, alias="afilcmpynm")

#     class Config:
#         from_attributes = True


# class openapi_corp_affilate_list(BaseModel):
#     affiliate_name_list: List[str]

#     class Config:
#         from_attributes = True


# class CompanyOverview(openapi_corp_affilate_list, openapi_corp_outline, dart_corp_info):
#     # 지역 : 국가,지역대,지역소 필요
#     # 중소기업, 벤처기업, 종속회사수, 주주수, 기업종업원수 여부 아직 없음
#     pass


class StockMarketDate(TypedDict):
    listDate: str
    delistDate: str


class Affiliate(TypedDict):
    corpCode: Optional[str]
    corpName: str


class OverviewDetailBase(BaseModel):
    stockName: str = Field(..., alias="stock_name")
    bizrNo: str = Field(..., alias="bizr_no")
    jurirNo: str = Field(..., alias="jurir_no")
    corpName: str = Field(..., alias="corp_name")
    corpNameEng: str = Field(..., alias="corp_name_eng")
    corpNameHistory: Optional[List[dict]] = Field(None, alias="corp_name_history")
    establishDate: str = Field(..., alias="est_dt")
    kospi: StockMarketDate
    kosdaq: StockMarketDate
    konex: StockMarketDate
    homepageUrl: Optional[str] = Field(None, alias="hm_url")
    phoneNum: str = Field(..., alias="phn_no")
    adress: str = Field(..., alias="adres")
    ceoName: str = Field(..., alias="ceo_nm")
    affiliateList: List[Affiliate] = Field(..., alias="affiliate_list")
    isSMCorp: Optional[bool] = Field(None, alias="smenpyn")
    isVenture: Optional[bool]
    subCorpNum: Optional[int] = Field(None, alias="sub_corp_num")
    shareholderNum: Optional[int] = Field(None, alias="shareholder_num")
    enployeeNum: int = Field(..., alias="enpempecnt")
    avgSalary: str = Field(..., alias="enppn1avgslryamt")
    auditorReportOpinion: Optional[str] = Field(None, alias="audtrptopnnctt")
    settleMonth: int = Field(..., alias="acc_mt")
    issuerRate: Optional[str]
    mainBiz: str = Field(..., alias="enpmainbiznm")
    classList: List[dict]

    class Config:
        from_attributes = True


class OverviewDetail(OverviewDetailBase):
    pass
