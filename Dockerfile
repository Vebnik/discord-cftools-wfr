FROM python:3.10

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry install