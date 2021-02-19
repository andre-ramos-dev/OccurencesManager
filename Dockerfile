FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y \
    python-pip \
    python-dev \
    libpq-dev \
    gettext \
    libreadline-dev \
    libssl-dev \
    libjpeg-dev \
    libfreetype6-dev \
    binutils \
    libproj-dev \
    gdal-bin \
    postgis

RUN pip install pip==21.0.1

RUN mkdir /code

ADD . /code/

VOLUME /code

WORKDIR /code/

RUN pip install -r requirements/base.pip

