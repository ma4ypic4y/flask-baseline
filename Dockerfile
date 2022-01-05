FROM python:3.6-slim

COPY . ./root

WORKDIR /root

RUN pip install -r requirements.txt