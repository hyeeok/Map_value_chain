from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel, Field, Json


class IndustryClassBase(BaseModel):
    industryClassCode: str = Field(..., alias="code")
    industryClassName: str = Field(..., alias="name")

    class Config:
        from_attributes = True


class IndustryClass(IndustryClassBase):
    industryClassId: int = Field(..., alias="id")


class IndustryClassName(BaseModel):
    industryClassName: str = Field(..., alias="name")


class IndustryClassList(BaseModel):
    length: int
    data: List[IndustryClass]

    class Config:
        from_attributes = True


class DomainBase(BaseModel):
    domainId: int = Field(..., alias="id")
    domainCode: str = Field(..., alias="code")
    domainName: str = Field(..., alias="name")


class Domain(DomainBase):
    classes: Optional[List[IndustryClass]] = []
    themes: Optional[List[IndustryClass]] = []


class FlowmapBase(BaseModel):
    node: List[Dict[str, Any]]
    edge: List[Dict[str, Any]]

    class Config:
        from_attributes = True


class Flowmap(FlowmapBase):
    pass


class FlowmapCreate(FlowmapBase):
    pass
