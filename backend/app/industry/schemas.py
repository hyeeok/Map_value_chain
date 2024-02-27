from typing import Dict, List, Optional

from pydantic import BaseModel, Field, validator


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


class Sub(ClassBase):
    subClassMajorName: Optional[str] = Field(..., alias="subclass_major_name")
    subClassMajorSeqlist: Optional[int] = Field(..., alias="subclass_major_seqlist")
    subClassMinorCode: Optional[str] = Field(..., alias="subclass_minor_code")
    subClassMinorName: Optional[str] = Field(..., alias="subclass_minor_name")
    subClassMinorMajorcode: Optional[str] = Field(..., alias="subclass_minor_majorcode")
    subClassMinorSeqlist: Optional[int] = Field(..., alias="subclass_minor_seqlist")
    subClassMinorSeqgrid: Optional[int] = Field(..., alias="subclass_minor_seqgrid")

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



class IndustryInfo(BaseModel):
    domainName: Optional[str] = Field(None, alias="domainName")
    industryClassName: Optional[str] = Field(None, alias="industryClassName")
    subClassMajorName: str = ""
    subClassMinorName: str = ""
    # subClassMajorName: str = Optional[str] = Field(None, alias="subClassMajorName")
    # subClassMinorName: str = Optional[str] = Field(None, alias="subClassMinorName")
    cnt: Dict[str, Optional[int]] = {}

    class Config:
        from_attributes = True

class IndustryInfoList(BaseModel):
    length: int
    data: List[IndustryInfo]

    class Config:
        from_attributes = True