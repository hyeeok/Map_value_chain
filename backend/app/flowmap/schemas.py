from typing import Any, Dict, List, Optional, Tuple, Union

from app.utils import to_camel
from pydantic import BaseModel, Field, Json


class CamelModel(BaseModel):
    class config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class IndustryClassBase(BaseModel):
    code: str
    name: str
    type: str
    domain_id: int
    domain_name: str
    domain_code: str


class IndustryClass(IndustryClassBase):
    id: int

    class Config:
        from_attributes = True


class IndustryClassList(BaseModel):
    length: int
    data: List[IndustryClass]

    class Config:
        from_attributes = True


class FlowmapBase(BaseModel):
    node: List[Dict[str, Any]]
    edge: List[Dict[str, Any]]

    class Config:
        from_attributes = True


class Flowmap(FlowmapBase):
    class Config:
        form_attributes = True


class DomainIndustryClass(BaseModel):
    industryClassId: int = Field(..., alias="id")
    industryClassCode: str = Field(..., alias="code")
    industryClassName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class DomainBase(BaseModel):
    domainId: int = Field(..., alias="id")
    domainCode: str = Field(..., alias="code")
    domainName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class Domain(DomainBase):
    classes: Optional[List[DomainIndustryClass]] = []
    themes: Optional[List[DomainIndustryClass]] = []

    class Config:
        from_attributes = True


class DomainList(CamelModel):
    length: int
    data: List[Union[Domain, None]]

    class Config:
        from_attributes = True
