FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

ENTRYPOINT [ "gunicorn", "-c", "gunicorn_config.py", "app:server" ]
