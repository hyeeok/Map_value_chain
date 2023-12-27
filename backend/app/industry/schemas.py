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
    industryClassSeqList: Optional[int] = Field(..., alias="industry_class_seq_list")
    industryClassSeqGrid: Optional[int] = Field(..., alias="industry_class_seq_grid")

    class Config:
        from_attributes = True


class SubMinor(ClassBase):
    subClassCode: Optional[str] = Field(..., alias="subclass_code")
    subClassName: Optional[str] = Field(..., alias="subclass_name")
    subClassIndustryclasscode: Optional[str] = Field(
        ..., alias="subclass_industryclasscode"
    )
    subClassMajorcode: Optional[str] = Field(..., alias="subclass_majorcode")
    subClassSeqlist: Optional[int] = Field(..., alias="subclass_seqlist")
    subClassSeqgrid: Optional[int] = Field(..., alias="subclass_seqgrid")

    class Config:
        from_attributes = True


class IndustryList(BaseModel):
    length: int
    data: List[Industry]

    class Config:
        from_attributes = True


class SubList(BaseModel):
    length: int
    data: List[SubMinor]

    class Config:
        from_attributes = True
