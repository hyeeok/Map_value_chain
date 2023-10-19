from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.flowmap.routers import router as flowmap_router

app = FastAPI()

# 허용할 오리진(출처) 목록
origins = ["http://127.0.0.1:3000", "http://localhost:3000","http://localhost","http://127.0.0.1"]

# CORS 미들웨어 추가해 오리진 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # 허용할 출처 목록
    allow_credentials=True, # 자격 증명 허용 여부
    allow_methods=["*"],  # 허용할 HTTP 메서드
    allow_headers=["*"],  # 허용할 HTTP 헤더
)

app.include_router(flowmap_router)