from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IndustryClassesBase(BaseModel):
    industryClassCode: str = Field(..., alias="industryClassCode")
    industryClassName: str = Field(..., alias="industryClassName")
    industryClassId: int = Field(..., alias="industryClassId")
    domainId: int = Field(..., alias="domainId")
    domainName: str = Field(..., alias="domainName")
    domainCode: str = Field(..., alias="domainCode")

    class Config:
        from_attributes = True


class IndustryClasses(IndustryClassesBase):
    pass


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
