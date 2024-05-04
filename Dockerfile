FROM python:3.13.0a5-alpine3.18
LABEL authors="zkwolf (PROJECT REBIRTH)"

RUN apk add curl && apk upgrade

COPY src /app/src
COPY requirements.txt /app/src/requirements.txt

WORKDIR /app/src

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/api/v1/healthcheck

ENTRYPOINT ["python", "start_app.py"]