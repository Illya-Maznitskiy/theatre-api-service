FROM python:3.12-alpine
LABEL maintainer="comercaleuros@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apk add --no-cache shadow && \
    adduser --disabled-password -H my_user && \
    mkdir -p /files/media && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

USER my_user
