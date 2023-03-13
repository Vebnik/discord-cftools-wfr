FROM python:3.11

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry install