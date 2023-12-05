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


class Affiliate(TypedDict):
    corpCode: Optional[str]
    corpName: str


class OverviewBase(BaseModel):
    corpCode: str = Field(..., alias="corp_code")
    stockName: Optional[str] = Field(None, alias="stock_name")
    bizrNo: Optional[str] = Field(None, alias="bizr_no")
    corpClass: str = Field(..., alias="corp_cls")
    stockCode: Optional[str] = Field(None, alias="stock_code")
    affiliateList: List[Affiliate] = Field([], alias="affiliate_list")
    ceoName: Optional[str] = Field(None, alias="ceo_nm")
    establishDate: Optional[str] = Field(None, alias="est_dt")
    adress: Optional[str] = Field(None, alias="adres")
    homepageUrl: Optional[str] = Field(None, alias="hm_url")

    class Config:
        from_attributes = True


class OverviewList(BaseModel):
    length: int
    data: List[OverviewBase]

    class Config:
        from_attributes = True


class SubCorp(TypedDict):
    # corpCode: Optional[str]
    corpName: str


class CeoNameHistory(TypedDict):
    seq: int
    ceoName: str
    update_date: str


class CorpNameHistory(TypedDict):
    seq: int
    corpName: str
    update_date: str


class OverviewDescriptionBase(BaseModel):
    stockName: Optional[str] = Field(None, alias="stock_name")
    stockCode: Optional[str] = Field(None, alias="stock_code")
    bizrNo: Optional[str] = Field(None, alias="bizr_no")
    jurirNo: str = Field(..., alias="jurir_no")
    corpName: str = Field(..., alias="corp_name")
    corpNameEng: str = Field(..., alias="corp_name_eng")
    corpNameHistory: Optional[List[CorpNameHistory]] = Field(
        None, alias="corp_name_history"
    )
    establishDate: Optional[str] = Field(None, alias="est_dt")
    corpClass: Optional[str] = Field(None, alias="corp_cls")
    listDate: Optional[str] = Field(None, alias="list_date")
    delistDate: Optional[str] = Field(None, alias="delist_date")
    homepageUrl: Optional[str] = Field(None, alias="hm_url")
    phoneNum: str = Field(..., alias="phn_no")
    adress: Optional[str] = Field(None, alias="adres")
    ceoName: Optional[str] = Field(None, alias="ceo_nm")
    ceoNameHistory: Optional[List[CeoNameHistory]] = Field(None, alias="ceo_nm_history")
    affiliateList: List[Affiliate] = Field(..., alias="affiliate_list")
    isSMCorp: Optional[str] = Field(None, alias="smenpyn")
    isVenture: Optional[str]
    subCorpList: Optional[List[SubCorp]] = Field(None, alias="sub_corp_list")
    employeeNum: int = Field(..., alias="enpempecnt")
    avgSalary: float = Field(..., alias="enppn1avgslryamt")
    auditorReportOpinion: Optional[str] = Field(None, alias="audtrptopnnctt")
    settleMonth: int = Field(..., alias="acc_mt")
    issuerRate: Optional[str]
    mainBiz: str = Field(..., alias="enpmainbiznm")
    classList: List[dict]

    class Config:
        from_attributes = True


class OverviewDescription(OverviewDescriptionBase):
    pass


class Shareholder(BaseModel):
    name: str = Field(..., alias="nm")
    relate: str = Field(..., alias="relate")
    stockKind: str = Field(..., alias="stock_knd")
    reportCode: str = Field(..., alias="reprt_code")
    basisStockCount: str = Field(..., alias="bsis_posesn_stock_co")
    basisStockRate: str = Field(..., alias="bsis_posesn_stock_qota_rt")
    endStockCount: str = Field(..., alias="trmend_posesn_stock_co")
    endStockRate: str = Field(..., alias="trmend_posesn_stock_qota_rt")
    note: str = Field(..., alias="rm")

    class Config:
        from_attributes = True


class OverviewShareholderList(BaseModel):
    length: int
    data: Optional[List[Shareholder]] = None

    class Config:
        from_attributes = True


class OverviewRelationBase(BaseModel):
    id: int
    industryClass: str
    corpName: str = Field(..., alias="corp_name")
    corpCode: Optional[str] = Field(None, alias="corp_code")
    vendorCorpName: str = Field(..., alias="vendor_corp_name")
    vendorCorpCode: Optional[str] = Field(None, alias="vendor_corp_code")
    vendorClass: str = Field(None, alias="vendor_class")
    industryClass: str = Field(None, alias="industry_class")
    updateDate: str = Field(None, alias="update_date")

    class Config:
        from_attributes = True


class OverviewRelationList(BaseModel):
    length: int
    data: List[OverviewRelationBase]

    class Config:
        from_attributes = True


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


class OverviewRelationsBase(BaseModel):
    pass


class OverviewRelations(OverviewRelationsBase):
    pass
