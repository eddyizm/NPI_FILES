#!/bin/bash

# podman set up to create pod, volumes and containers. 
echo "Creating podman volume npi_files_dbdata for postgres"
podman volume create npi_files_dbdata

# add 5432 if you want to expose postgres during development
echo "Creating infra pod with exposed ports 8080/8081"
podman pod create -p 8080:8000 -p 5432:5432 --name=npi_file
# this port is only for local dev, don't want ot expose this when putting on the server.
# -p 5432:5432
echo "Starting npi file pod..."
podman pod start npi_file 

# run postgres db
echo "Standing up postgres..."
podman run -d --pod=npi_file -v npi_files_dbdata:/var/lib/postgresql/data --env-file backend/.env docker.io/postgres:latest


# containerize django api
echo "Building django container..."
podman build -t npi_backend -f backend_docker

echo "Spin up django"
podman run -d --pod=npi_file --name=npi_backend_django npi_backend

# TODO 
# PENDING DOMAIN
# Add data domain for certificates
# echo "Starting Caddy webserver container in pod"
# podman run -d --pod=npi_file \
#     -v $PWD/Caddyfile:/etc/caddy/Caddyfile:z \
#     -v letsencrypt:/data \

# add volume to store file data - this should probably be s3 or something along those lines in the future.
