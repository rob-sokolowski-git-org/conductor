FROM python:3.8-slim

# NB: gcc and dev libs are required for installing data-science packages like scikit-learn
USER root
RUN apt-get update
RUN apt-get install -y \
    gcc \
    curl \
    python3-dev \
    python3-pip \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    g++

# Don't run rest as root
RUN useradd -ms /bin/bash appuser
USER appuser
WORKDIR /code

RUN pip install --user --upgrade pip
ENV PATH="${PATH}:/home/appuser/.local/bin"
RUN pip install --user pip-tools

RUN mkdir /home/appuser/code
RUN mkdir /home/appuser/install
RUN mkdir /home/appuser/.secrets
WORKDIR /home/appuser/install
COPY ./requirements.txt ./requirements.txt
RUN pip install --user -r ./requirements.txt

WORKDIR /home/appuser/code
