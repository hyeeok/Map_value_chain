FROM python:3.10.9-slim
WORKDIR /app

RUN apt-get -y update
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get install curl -y

COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
