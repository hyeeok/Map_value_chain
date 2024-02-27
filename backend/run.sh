# 레디스 서버 실행
redis-server --daemonize yes

# 유비콘 실행
uvicorn main:app --host 0.0.0.0 --port 8000
