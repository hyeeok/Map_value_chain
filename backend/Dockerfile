FROM python:3.10.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["sh", "-c", "redis-server --daemonize yes && uvicorn main:app --host 0.0.0.0 --port 8000"]
