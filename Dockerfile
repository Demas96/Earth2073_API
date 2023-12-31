FROM python:3

WORKDIR /Fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .