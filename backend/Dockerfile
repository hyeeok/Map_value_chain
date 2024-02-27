FROM python:3.10.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

# 레디스 서버 설치
RUN apt-get update && apt-get install -y redis-server

# 레디스 서버 및 유비콘 실행을 위한 스크립트 파일 복사
COPY run.sh .
RUN chmod +x run.sh

# 컨테이너 실행 시 스크립트 파일 실행
ENTRYPOINT ["./run.sh"]
