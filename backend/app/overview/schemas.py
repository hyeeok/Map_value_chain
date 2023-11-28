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
    corpClass: str = Field(..., alias="corp_cls")
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


class Affiliate(TypedDict):
    # corpCode: Optional[str]
    corpName: str


class SubCorp(TypedDict):
    # corpCode: Optional[str]
    corpName: str


class OverviewDescriptionBase(BaseModel):
    stockName: str = Field(..., alias="stock_name")
    stockCode: Optional[str] = Field(..., alias="stock_code")
    bizrNo: str = Field(..., alias="bizr_no")
    jurirNo: str = Field(..., alias="jurir_no")
    corpName: str = Field(..., alias="corp_name")
    corpNameEng: str = Field(..., alias="corp_name_eng")
    corpNameHistory: Optional[List[dict]] = Field(None, alias="corp_name_history")
    establishDate: str = Field(..., alias="est_dt")
    corpClass: Optional[str] = Field(None, alias="corp_cls")
    listDate: Optional[str] = Field(None, alias="list_date")
    delistDate: Optional[str] = Field(None, alias="delist_date")
    homepageUrl: Optional[str] = Field(None, alias="hm_url")
    phoneNum: str = Field(..., alias="phn_no")
    adress: str = Field(..., alias="adres")
    ceoName: str = Field(..., alias="ceo_nm")
    affiliateList: List[Affiliate] = Field(..., alias="affiliate_list")
    isSMCorp: Optional[str] = Field(None, alias="smenpyn")
    isVenture: Optional[str]
    subCorpList: Optional[List[SubCorp]] = Field(None, alias="sub_corp_list")
    shareholderNum: Optional[int] = Field(None, alias="shareholder_num")
    employeeNum: int = Field(..., alias="enpempecnt")
    avgSalary: str = Field(..., alias="enppn1avgslryamt")
    auditorReportOpinion: Optional[str] = Field(None, alias="audtrptopnnctt")
    settleMonth: int = Field(..., alias="acc_mt")
    issuerRate: Optional[str]
    mainBiz: str = Field(..., alias="enpmainbiznm")
    classList: List[dict]

    class Config:
        from_attributes = True


class OverviewDescription(OverviewDescriptionBase):
    pass


class OverviewFinancialsBase(BaseModel):
    # 시가총액(전체)

    # 발행주식수
    listShrs: str = Field(..., alias="list_shrs")

    # 자기주식수
    # 액면가
    parval: str = Field(..., alias="parval")

    # 발행주식수(보통주)
    # 주가(보통주)
    closePrice: str = Field(..., alias="close_price")

    # 발행주식수(우선주)
    # 주가(우선주)

    # 자산총계
    # thstrmAmount: str = Field(..., alias="thstrm_amount")

    # 통화단위
    # currency: str = Field(..., alias="currency")

    # 유동자산
    # 현금및현금성자산
    # 매출채권
    # 단기금융상품
    # 단기금융자산

    # 등등

    class Config:
        from_attributes = True


class OverviewFinancials(OverviewFinancialsBase):
    pass
