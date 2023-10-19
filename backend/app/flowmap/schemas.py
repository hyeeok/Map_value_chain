from pydantic import BaseModel
import stringcase
from typing import Union, List

class IndustryClassBase(BaseModel):
    code: str
    name: str
    type: str
    domain_code: str


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