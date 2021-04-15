FROM python:3.9-alpine

WORKDIR /usr/src/api
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN apk update && apk add gcc musl-dev libffi-dev cargo openssl-dev make
RUN pip install --upgrade pip; pip install poetry; poetry config virtualenvs.create false; poetry install
CMD ["uvicorn", "apimeta:app", "--port", "8001", "--host", "0.0.0.0"]