FROM python:3.11-alpine

RUN pip install --upgrade pip

RUN apk add postgresql-client build-base postgresql-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY Site /Site

WORKDIR /Site

RUN python manage.py collectstatic

ENV PYTHONUNBUFFERED=1

COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]