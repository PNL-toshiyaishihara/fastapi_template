FROM python:3.10-buster as builder
COPY ./requirements.lock /app/requirements.lock
RUN pip install --no-cache-dir --user -r /app/requirements.lock

FROM python:3.10-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Tokyo

COPY --from=builder /root/.local /root/.local

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    git \
    gettext \
    build-essential \
    libpq-dev \
    openssh-client \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && truncate -s 0 /var/log/*log

ENV APP_HOME=/app
WORKDIR $APP_HOME

COPY ./api                  /app/api/
COPY ./base                 /app/base
COPY ./server               /app/server
COPY ./app.py               /app
