import requests
from get_monthly_url import GetURL

BASE_URL='https://download.cms.gov'
BASE_PATH='nppes'
INFO_URL=f'{BASE_URL}/{BASE_PATH}/NPI_Files.html'


def download_file(url, target_path):
    # TODO implement check to make we the file doesn't already exists or we already didn't DL and dumped it into the db.
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    with open(target_path, 'wb') as f:
        f.write(response.content)
    print("Download completed!")


def download_deactivated_npi_report_zip():
    """'target_path' is the directory of your project"""
    # TODO Needs a way to change the URL every month.
    #class created in get_monthly_url.py
    class_object = GetURL()

    # This URL will change every second Monday of the month.
    # get_monthly_url() gets the second Monday of the month and rewrites the URL accordingly
    file_name = class_object.get_monthly_url() # filenamne to be generated dynamically from scrape
    
    url = f'{BASE_URL}/{BASE_PATH}/{file_name}'
    target_path = f'tmp/{file_name}'

    download_file(url, target_path)


def get_page_contents(url: str) -> str:
    """Return main page contents as text. grep results to find pattern or use beautitul soup
        This should allow use to find all the file names we need, check against the DB or some other data store to see if we have
        received that file yet and retrieve to extract the data.
    """
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    get_page_contents(INFO_URL) # redirected output to page.html for sample
    download_deactivated_npi_report_zip()
