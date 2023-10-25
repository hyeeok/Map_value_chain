from typing import Any, Dict, List, Optional, Tuple, Union

import stringcase
from pydantic import BaseModel, Json


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
        stringcase.camelcase = True
