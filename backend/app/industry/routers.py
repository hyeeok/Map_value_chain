import io
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from openpyxl import Workbook 
from sqlalchemy.orm import Session


from app.database import get_dev_db
from app.database import get_mvc_db

from . import crud
from .schemas import *

router = APIRouter(prefix="/industry")


@router.get("", response_model=IndustryList, response_model_by_alias=False)
def read_industry_class(db: Session = Depends(get_dev_db)):
    try:
        result = crud.get_industry_class_list(db=db)
        return {"length": len(result), "data": result}

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download")
async def download_industry(db: Session = Depends(get_dev_db)):

    data = crud.get_industry_class_download_format(db)
    
    wb = Workbook()
    ws = wb.active

    ws.append(["도메인 코드", "도메인 명", "도메인 그룹", "산업분류 코드", "산업분류 명", "산업분류 유형"])

    for entry in data:
        row = [
            entry["domainCode"],
            entry["domainName"],
            entry["domainDivision"],
            entry["industryClassCode"],
            entry["industryClassName"],
            entry["industryClassType"],
        ]
        ws.append(row)

    file_stream = io.BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)
    
    return StreamingResponse(file_stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=industry_class.xlsx"})


@router.get("/subclass", response_model=SubList, response_model_by_alias=False)
def read_sub_class(db: Session = Depends(get_dev_db)):
    try:
        result = crud.get_sub_class_list(db=db)
        return {"length": len(result), "data": result}

    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get("/info", response_model=IndustryInfoList, response_model_by_alias=False)
def read_industry_info(db: Session = Depends(get_mvc_db)):
    try:
        result = crud.get_industry_class_info_list(db=db)
        return {"length": len(result), "data": result}
    except Exception as e:
        print(repr(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/info/download")
async def download_industry_info(db: Session = Depends(get_mvc_db)):

    data = crud.get_industry_class_info_list(db)
    
    wb = Workbook()
    ws = wb.active

    ws.append(["Index", "도메인 명", "산업분류 명", "합계", "코스피", "코스닥", "코넥스", "비상장외감", "비외감", "합계 비율", "코스피 비율", "코스닥 비율", "코넥스 비율", "비상장외감 비율", "비외감 비율"])
    # ws.append(["Index", "Domain Name", "Industry Class Name", "Sub Major Class Name", "Sub Minor Class Name", "TOTAL", "Y", "K", "N", "비상장외감", "비외감", "TOTAL Rate", "Y Rate", "K Rate", "N Rate", "비상장외감 Rate", "비외감 Rate"])

    for index, entry in enumerate(data, start=1):
        row = [
            index,
            entry["domainName"],
            entry["industryClassName"],
            # entry["subClassMajorName"],
            # entry["subClassMinorName"],
            entry["cnt"]["TOTAL"],
            entry["cnt"]["Y"],
            entry["cnt"]["K"],
            entry["cnt"]["N"],
            entry["cnt"]["비상장외감"],
            entry["cnt"]["비외감"],
            entry["rate"]["TOTAL"],
            entry["rate"]["Y"],
            entry["rate"]["K"],
            entry["rate"]["N"],
            entry["rate"]["비상장외감"],
            entry["rate"]["비외감"],
        ]
        ws.append(row)

    for column in ws.columns:
        for cell in column:
            if isinstance(cell.value, float):
                cell.number_format = '0.000000'
                
    file_stream = io.BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)
    
    return StreamingResponse(file_stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=industry_info.xlsx"})
