FROM python:3.8-alpine

RUN apk update && apk add git && apk add python3-dev && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt ./app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/
