FROM python:3.9-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libev-dev \
    autoconf \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get purge -y --auto-remove \
    gcc \
    libffi-dev \
    libev-dev \
    autoconf \
    pkg-config

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]