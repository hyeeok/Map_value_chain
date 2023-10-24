from pydantic import BaseModel
import stringcase
from typing import Union, List, Optional, Tuple


from pydantic import Json


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
    data: List[Tuple[List[int], List[int]]]

    class Config:
        from_attributes = True


class Flowmap(FlowmapBase):
    id: int
    industry_class_id: Optional[int]
    domain_id: Optional[int]

    class Config:
        from_attributes = True
