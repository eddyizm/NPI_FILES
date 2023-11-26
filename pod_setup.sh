#!/bin/bash

# podman set up to create pod, volumes and containers. 

echo "Creating podman volume npi_files_dbdata for postgres"
podman volume create npi_files_dbdata

# add 5432 if you want to expose postgres during development
echo "Creating infra pod with exposed ports 8080/8081"
podman pod create -p 8080:80 -p 8081:443 --name=npi_file

# run postgres db
echo "Standing up postgres..."
podman run -d --pod=npi_file -v dbdata:/var/lib/postgresql/data -p 5432:5432 --env-file backend/npi_api/.env docker.io/postgres:latest

# todo 
# add volume to store file data - this should probably be s3 or something along those lines in the future.
# containerize django api
# containerize front end
# add webserver nginx container to tie it all together
