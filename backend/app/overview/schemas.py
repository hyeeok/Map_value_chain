from typing import List, Optional, TypedDict

from pydantic import BaseModel, Field
from typing_extensions import TypedDict


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


from typing import Optional, List
from pydantic import BaseModel, Field


class OverviewDescriptionBase(BaseModel):
    stockName: Optional[str] = Field(None, alias="stock_name")
    stockCode: Optional[str] = Field(None, alias="stock_code")
    bizrNo: Optional[str] = Field(None, alias="bizr_no")
    jurirNo: Optional[str] = Field(None, alias="jurir_no")
    corpName: Optional[str] = Field(None, alias="corp_name")
    corpNameEng: Optional[str] = Field(None, alias="corp_name_eng")
    corpNameHistory: Optional[List[CorpNameHistory]] = Field(
        None, alias="corp_name_history"
    )
    establishDate: Optional[str] = Field(None, alias="est_dt")
    corpClass: Optional[str] = Field(None, alias="corp_cls")
    listDate: Optional[str] = Field(None, alias="list_date")
    delistDate: Optional[str] = Field(None, alias="delist_date")
    homepageUrl: Optional[str] = Field(None, alias="hm_url")
    phoneNum: Optional[str] = Field(None, alias="phn_no")
    adress: Optional[str] = Field(None, alias="adres")
    ceoName: Optional[str] = Field(None, alias="ceo_nm")
    ceoNameHistory: Optional[List[CeoNameHistory]] = Field(None, alias="ceo_nm_history")
    affiliateList: Optional[List[Affiliate]] = Field(None, alias="affiliate_list")
    isSMCorp: Optional[str] = Field(None, alias="smenpyn")
    isVenture: Optional[str] = Field(None, alias="isVenture")
    subCorpList: Optional[List[SubCorp]] = Field(None, alias="sub_corp_list")
    employeeNum: Optional[int] = Field(None, alias="enpempecnt")
    avgSalary: Optional[float] = Field(None, alias="enppn1avgslryamt")
    auditorReportOpinion: Optional[str] = Field(None, alias="audtrptopnnctt")
    settleMonth: Optional[int] = Field(None, alias="acc_mt")
    issuerRate: Optional[str] = Field(None, alias="issuerRate")
    mainBiz: Optional[str] = Field(None, alias="enpmainbiznm")
    classList: Optional[List[dict]] = None


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
    krxOpenapiStockPriceId: str = Field(..., alias="krx_openapi_stock_price_id")
    isuNm: Optional[str] = Field(..., alias="isu_nm")
    mktcap: int = Field(..., alias="mktcap")
    mktcapDifferencePercentage: Optional[float] = Field(
        ..., alias="mktcap_difference_percentage"
    )

    class Config:
        from_attributes = True


class OverviewFinancialList(BaseModel):
    data: List[OverviewFinancialsBase]

    class Config:
        from_attributes = True


class OverviewFinancials(OverviewFinancialsBase):
    pass


class OverviewRelationsBase(BaseModel):
    pass


class OverviewRelations(OverviewRelationsBase):
    pass
