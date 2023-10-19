from pydantic import BaseModel
import stringcase
from typing import Union, List, Optional

from pydantic import Json


class IndustryClassBase(BaseModel):
    code: str
    name: str
    type: str
    domain_id: str


class IndustryClass(IndustryClassBase):
    id: int

    class Config:
        orm_mode = True
        alias_generator = stringcase.camelcase


class IndustryClassList(BaseModel):
    length: int
    data: List[Union[IndustryClass, None]]

    class Config:
        orm_mode = True
        alias_generator = stringcase.camelcase


class FlowmapBase(BaseModel):
    node: Json
    edge: Json
    industry_class_id: Optional[int]


class Flowmap(FlowmapBase):
    class Config:
        orm_mode = True
        alias_generator = stringcase.camelcase
