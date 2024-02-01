# NPI_FILES

repo to automate NPI file download, extract and load into a database and create an api for endpoint

## Podman setup in script

work in progress... `pod_setup.sh`

## Local Development for Django

The instructions below are specific to local Postgres environment. This is the current default method.

Once the application is more flushed out, this repo will be updated for instructions to containerize with a Postgres database.

## Prerequisite

This requirement will have you create a copy of `.env.dummy` and update the file with appropriate values so you don't check in any passwords or settings. These values are referenced in Django's `settings.py` file

1. Navigate to `NPI_FILES/backend`

2. Create a copy of `.env.dummy`  
   `cp .env.dummy .env`

3. Update all the relevant fields with your local postgres in `backend/.env`.

## Backend setup

1.  Ensure you are in `NPI_FILES directory` and create virtual environment
    `python -m venv env`

2.  Activate your virtual environment `source env/bin/activate`
    **NOTE: Windows may use this env/Scripts/activate path instead**

3.  Install requirements
    `pip install -r backend/requirements.txt`

4.  Make db migrations
    `python backend/manage.py migrate`

5.  Create super user before logging in to admin
    `python backend/manage.py createsuperuser`

6.  Launch Django
    `python backend/manage.py runserver`
