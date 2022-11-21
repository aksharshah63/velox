FROM python:3.9-slim-buster

ENV PIP_NO_CACHE_DIR=1
ENV APP_HOME /webapp

WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get install -y ffmpeg libsm6 libxext6 build-essential cmake
RUN pip install --upgrade pip
COPY velox_backend/requirements.txt .
RUN pip install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

COPY velox_backend .

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 --forwarded-allow-ips="*" velox.wsgi:application