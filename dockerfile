FROM python:3.11-slim

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r ./app/requirements.txt

COPY . /app

WORKDIR /app/src