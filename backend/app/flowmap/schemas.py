from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IndustryClassBase(BaseModel):
    domainCode: str = Field(..., alias="domain_code")
    domainName: str = Field(..., alias="domain_name")
    domainDivision: int = Field(..., alias="domain_division")
    industryClassCode: str = Field(..., alias="industry_class_code")
    industryClassName: str = Field(..., alias="industry_class_name")
    industryClassType: str = Field(..., alias="industry_class_type")

    class Config:
        from_attributes = True


class IndustryClass(IndustryClassBase):
    pass


class IndustryClassList(BaseModel):
    length: int
    data: List[IndustryClass]

    class Config:
        from_attributes = True


class FlowmapList(BaseModel):
    node: List[Dict[str, Any]]
    edge: List[Dict[str, Any]]

    class Config:
        from_attributes = True


class FlowmapBase(BaseModel):
    node: Dict[str, Any]
    edge: Dict[str, Any]


class FlowmapCreate(FlowmapList):
    pass
