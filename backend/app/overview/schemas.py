from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel, Field, Json


class IndustryClassBase(BaseModel):
    industryClassCode: str = Field(..., alias="code")
    industryClassName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class IndustryClass(IndustryClassBase):
    industryClassId: int = Field(..., alias="id")
    domainId: Optional[int] = Field(..., alias="domain_id")
    domainCode: Optional[str] = Field(..., alias="domain_code")
    domainName: Optional[str] = Field(..., alias="domain_name")


class IndustryClassList(BaseModel):
    length: int
    data: List[IndustryClass]

    class Config:
        from_attributes = True


class DomainBase(BaseModel):
    domainId: int = Field(..., alias="id")
    domainCode: str = Field(..., alias="code")
    domainName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class Domain(DomainBase):
    classes: Optional[List[IndustryClass]] = []
    themes: Optional[List[IndustryClass]] = []


class DomainList(BaseModel):
    length: int
    data: List[Union[Domain, None]]

    class Config:
        from_attributes = True


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


class mvc_fake_data(BaseModel):
    corpCode: Optional[str] = Field(..., alias="corp_code")
    firmName: Optional[str] = Field(..., alias="firm")
    bizrNo: Optional[str] = Field(..., alias="bizr_no")
    jurirNo: Optional[str] = Field(..., alias="corp_cls")
    stockCode: Optional[str] = Field(..., alias="stock_code")
    # conglomerateName: Optional[str] = Field(..., alias="stock_name")
    # ceoName: Optional[str] = Field(..., alias="ceo_nm")
    establishDate: Optional[str] = Field(..., alias="bsns_year")
    adress1: Optional[str] = Field(..., alias="adres_1")
    adress2: Optional[str] = Field(..., alias="adres_2")
    # hompageUrl: Optional[str] = Field(..., alias="hm_url")

    class Config:
        from_attributes = True


class mvc_fake_data_list(BaseModel):
    length: int
    data: List[mvc_fake_data]

    class Config:
        from_attributes = True


class dart_corp_info(BaseModel):
    firm: str = Field(..., alias="stock_name")
    bizr_no: str = Field(..., alias="bizr_no")
    jurir_no: str = Field(..., alias="jurir_no")
    stock_code: Optional[str] = Field(None, alias="stock_code")
    corp_cls: str = Field(..., alias="corp_cls")
    corp_name: str = Field(..., alias="corp_name")
    corp_name_eng: str = Field(..., alias="corp_name_eng")
    ceo_nm: str = Field(..., alias="ceo_nm")
    est_dt: str = Field(..., alias="est_dt")
    acc_mt: str = Field(..., alias="acc_mt")

    class Config:
        from_attributes = True


class openapi_corp_outline(BaseModel):
    enpkosdaqlstgdt: Union[str, None] = Field(..., alias="enpkosdaqlstgdt")
    enpxchglstgdt: Union[str, None] = Field(..., alias="enpxchglstgdt")
    enpkosdaqlstgaboldt: Union[str, None] = Field(..., alias="enpkosdaqlstgaboldt")
    enpkrxlstgdt: Union[str, None] = Field(..., alias="enpkrxlstgdt")
    enpkrxlstgaboldt: Union[str, None] = Field(..., alias="enpkrxlstgaboldt")
    enpempecnt: Union[str, None] = Field(..., alias="enpempecnt")
    empeavgcnwktermctt: Union[str, None] = Field(..., alias="empeavgcnwktermctt")
    enppn1avgslryamt: Union[str, None] = Field(..., alias="enppn1avgslryamt")
    actnaudpnnm: Union[str, None] = Field(..., alias="actnaudpnnm")
    audtrptopnnctt: Union[str, None] = Field(..., alias="audtrptopnnctt")
    enpmainbiznm: Union[str, None] = Field(..., alias="enpmainbiznm")

    class Config:
        from_attributes = True


class openapi_corp_affiliate(BaseModel):
    afilcmpynm: Union[str, None] = Field(..., alias="afilcmpynm")

    class Config:
        from_attributes = True


class CompanyDetailResponse(BaseModel):
    dart_corp_info_data: dart_corp_info
    openapi_outline_data: Optional[List[openapi_corp_outline]]
    openapi_affiliate_data: Optional[List[openapi_corp_affiliate]]

    class Config:
        from_attributes = True
