from pydantic import BaseModel, Json
import stringcase
from typing import Union, List, Optional, Tuple, Dict, Any


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
    node: List[Dict[str, Any]]
    edge: List[Dict[str, Any]]

    class Config:
        from_attributes = True
