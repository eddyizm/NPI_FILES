# NPI_FILES
repo to automate NPI file download, extract and load into a database and create an api for endpoint

## Podman setup in script  

work in progress... `pod_setup.sh`

## Local Development for Django  

Need to set up postgres, either locally or in a container. The container is my choice as it makes it easier when testing with the containerized django app.

This requirement will have you update the `.env.dummy` file with appropriate values and rename it to `.env` so you don't check in any passwords or settings. 

These values are references in django's `settings.py` file
    
    # create virtual environment
    python -m venv env
    # then activate it
    source env/bin/activate
    # windows may use this env/Scripts/activate path instead
    
    # install requirements  
    pip install -r backend/requirements.txt

    # make db migrations 
    python backend/manage.py migrate
    
    # launch django
    python backend/manage.py runserver 

I suspect you need to create a super user here before run server or soon after.

`python manage.py createsuperuser`

---
# Custom Management Commands

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
    