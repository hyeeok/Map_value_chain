from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IndustryClassBase(BaseModel):
    industryClassCode: str = Field(..., alias="code")
    industryClassName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class IndustryClass(IndustryClassBase):
    industryClassId: int = Field(..., alias="id")


class DomainBase(BaseModel):
    domainId: int = Field(..., alias="id")
    domainCode: str = Field(..., alias="code")
    domainName: str = Field(..., alias="name")


class Domain(DomainBase):
    classes: Optional[List[IndustryClass]] = []
    themes: Optional[List[IndustryClass]] = []


class IndustryClasses(IndustryClass, DomainBase):
    pass


class IndustryClassList(BaseModel):
    length: int
    data: List[IndustryClasses]

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
