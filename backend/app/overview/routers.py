from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Union

from app.database import get_db
from . import crud
from .schemas import CompanyList, DepsList

router = APIRouter(prefix="/overview")


@router.get("", response_model=CompanyList)
async def read_company_basic(
    term: str = Query(..., description="Search term"),
    option: str = Query(..., description="Search option: 'name' or 'other'"),
    db: Session = Depends(get_db),
):
    result = crud.get_company_basic(term=term, option=option, db=db)
    return {"length": len(result), "data": result}


@router.get("/search", response_model=List[Dict[str, Union[int, str]]])
async def read_company_items_by_option(
    term: str = Query(..., description="Search term"),
    option: str = Query(..., description="Search option: 'name' or 'other'"),
    db: Session = Depends(get_db),
):
    items = crud.get_company_items_by_option(term=term, option=option, db=db)
    return items


@router.get("/index", response_model=DepsList, response_model_by_alias=False)
def read_deps(db: Session = Depends(get_db)):
    result = crud.get_deps(db=db)
    return {"length": len(result), "data": result}
