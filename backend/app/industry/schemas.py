from typing import List, Optional

from pydantic import BaseModel, Field


class ClassBase(BaseModel):
    domainCode: Optional[str] = Field(..., alias="domain_code")
    domainName: Optional[str] = Field(..., alias="domain_name")
    industryClassCode: Optional[str] = Field(..., alias="industry_class_code")
    industryClassName: Optional[str] = Field(..., alias="industry_class_name")

    class Config:
        from_attributes = True


class Industry(ClassBase):
    domainDivision: Optional[str] = Field(..., alias="domain_division")
    domainSeq: Optional[int] = Field(..., alias="domain_seq")
    industryClassType: Optional[str] = Field(..., alias="industry_class_type")
    industryClassSeq: Optional[int] = Field(..., alias="industry_class_seq")

    class Config:
        from_attributes = True


class Sub(ClassBase):
    subClassCode: Optional[str] = Field(..., alias="sub_class_code")
    subClassName: Optional[str] = Field(..., alias="sub_class_name")
    subClassLevel: Optional[int] = Field(..., alias="sub_class_level")

    class Config:
        from_attributes = True


class IndustryList(BaseModel):
    length: int
    data: List[Industry]

    class Config:
        from_attributes = True


class SubList(BaseModel):
    length: int
    data: List[Sub]

    class Config:
        from_attributes = True
