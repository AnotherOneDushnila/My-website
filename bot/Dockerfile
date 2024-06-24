FROM python:3.11-alpine

RUN pip install --upgrade pip

RUN apk add postgresql-client build-base postgresql-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY Bot /Bot

WORKDIR /Bot

CMD [ "python", "main.py"]