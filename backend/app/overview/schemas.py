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


class Company(BaseModel):
    companyName: Optional[str] = Field(..., alias="name")
    registrationNumber: Optional[str] = Field(..., alias="registration_number")
    corporateType: Optional[str] = Field(..., alias="corporate_type")
    stockCode: Optional[str] = Field(..., alias="stock_code")
    subsidiaryMock: Optional[bool] = Field(..., alias="subsidiary_mock")
    ceoName: Optional[str] = Field(..., alias="ceo_name")
    establishmentDate: Optional[str] = Field(..., alias="establishment_date")
    region: Optional[str] = Field(..., alias="region")
    website: Optional[str] = Field(..., alias="website")

    class Config:
        from_attributes = True


class CompanyList(BaseModel):
    length: int
    data: List[Company]

    class Config:
        from_attributes = True
