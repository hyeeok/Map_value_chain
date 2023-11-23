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

    class Config:
        from_attributes = True


class dart_corp_info(BaseModel):
    corp_name: str = Field(..., alias="corp_name")
    bizr_no: str = Field(..., alias="bizr_no")
    jurir_no: str = Field(..., alias="jurir_no")
    corp_name_eng: str = Field(..., alias="corp_name_eng")
    ceo_nm: str = Field(..., alias="ceo_nm")
    est_dt: str = Field(..., alias="est_dt")
    listing_date: str
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
    afilcmpynm: str = Field(None, alias="afilcmpynm")

    class Config:
        from_attributes = True


class openapi_corp_affilate_list(BaseModel):
    affiliate_name_list: List[str]

    class Config:
        from_attributes = True


class CompanyOverview(openapi_corp_affilate_list, openapi_corp_outline, dart_corp_info):
    # 지역 : 국가,지역대,지역소 필요
    # 중소기업, 벤처기업, 종속회사수, 주주수, 기업종업원수 여부 아직 없음
    pass
