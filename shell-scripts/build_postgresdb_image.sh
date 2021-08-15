#!/bin/bash

docker build -t postgres-db:latest \
    --file Dockerfile-Postgres \
    .
