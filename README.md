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
