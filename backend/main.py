# from app.database import SessionLocal
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import get_dev_db
from app.flowmap.routers import router as flowmap_router
from app.flowmap.utils.init_db import load_csv_to_db
from app.overview.routers import router as overview_router

# async def initialize_db():
#     filepath = "./source/mvc_map.csv"
#     db = SessionLocal()
#     load_csv_to_db(filepath, db)
#     db.commit()
#     db.close()


# async def initialize_db(db=Depends(get_dev_db)):
#     filepath = "./source/mvc_map.csv"
#     load_csv_to_db(filepath, db)
#     db.commit()
#     db.close()


# async def wait_for_postgres():
#     while True:
#         try:
#             await initialize_db()
#             print("Connected to PostgreSQL")
#             return

#         except Exception as e:
#             print(f"Waiting for PostgreSQL: {e}")
#             await asyncio.sleep(1)


# async def lifespan(app: FastAPI):
#     asyncio.create_task(wait_for_postgres())
#     await initialize_db()
#     yield


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await initialize_db()
#     yield


# app = FastAPI(lifespan=lifespan, redoc_url=None)
app = FastAPI(redoc_url=None)

# 허용할 오리진(출처) 목록
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
]

# CORS 미들웨어 추가해 오리진 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 허용할 출처 목록
    allow_credentials=True,  # 자격 증명 허용 여부
    allow_methods=["*"],  # 허용할 HTTP 메서드
    allow_headers=["*"],  # 허용할 HTTP 헤더
)

app.include_router(flowmap_router)
app.include_router(overview_router)
