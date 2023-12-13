from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.industry.routers import router as industry_router
from app.overview.routers import router as overview_router

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

app.include_router(industry_router)
app.include_router(overview_router)
