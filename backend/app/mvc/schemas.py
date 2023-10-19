from pydantic import BaseModel
import stringcase


class IndustryBase(BaseModel):
    code: str
    name: str
    type: str
    domain_code: str


class Industry(IndustryBase):
    id: int

    class Config:
        orm_mode = True
        alias_generator = stringcase.camelcase
