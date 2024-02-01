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

2.  Activate your virtual environment  
    `source env/bin/activate`  
    **NOTE: Windows may use this env/Scripts/activate path instead**

3.  Install requirements  
    `pip install -r backend/requirements.txt`

4.  Make db migrations  
    `python backend/manage.py migrate`

5.  Create super user before logging in to admin  
    `python backend/manage.py createsuperuser`

6.  Launch Django
    `python backend/manage.py runserver`

---
## Custom Management Commands

These commands are used to run automated tasks. The order in this sense matters as later this can be used with an orchestration tool. 

1. fetch_urls 
    - scrapes urls of npi zip files to download
2. get_download 
    - this one is getting list of files to download
    - downloading files that have yet to be downloaded
    - then loading them up to the db.
    - needs work and to be cleaned up. 
3. load_large_csv  
    - This function upload csv to a target table using pg command.
    - need to remember why i did this, probably for the 9gb file

misc. 

4. hello_world
    - just a dummy command to verify things are working and build use as a template.
    

