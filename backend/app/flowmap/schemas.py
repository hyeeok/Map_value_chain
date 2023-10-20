from pydantic import BaseModel
import stringcase
from typing import Union, List, Optional

from pydantic import Json


class IndustryClassBase(BaseModel):
    code: str
    name: str
    type: str
    domain_id: int


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
    node: List[int]
    edge: List[int]
    industry_class_id: Optional[int]

    class Config:
        from_attributes = True


class Flowmap(FlowmapBase):
    id: int
    domain_id: int

    class Config:
        from_attributes = True


class FlowmapList(BaseModel):
    length: int
    data: List[FlowmapBase]

    class Config:
        from_attributes = True
