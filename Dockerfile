# Step 1: Build stage
FROM python:3.10.15-slim-bookworm AS build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install python3-dev gcc default-libmysqlclient-dev libmariadb-dev-compat build-essential pkg-config libpq-dev -y

WORKDIR /app

RUN pip install -U pip setuptools wheel
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Step 2: Production stage
FROM python:3.10.15-slim-bookworm

WORKDIR /MechSimVault

RUN apt update && apt install -y \
    mariadb-client

COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY apps/ ./apps/
COPY MechSimVault/ ./MechSimVault/
COPY media/ ./media/
COPY manage.py gunicorn_config.py container-entrypoint.sh ./
RUN chmod +x container-entrypoint.sh


EXPOSE 8000

ENTRYPOINT ["sh", "./container-entrypoint.sh"]
