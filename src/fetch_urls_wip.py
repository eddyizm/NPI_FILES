import requests
import re
import urllib.parse
import json

def fetch_current_zip_urls(base_url):
    response = requests.get(base_url)
    relative_urls = re.findall(r"href='(\./NPPES_Data_Dissemination_[^']*?\.zip)'", response.text)
    current_urls = [urllib.parse.urljoin(base_url, url) for url in relative_urls]
    return current_urls

def load_stored_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_urls(file_path, urls):
    with open(file_path, 'w') as file:
        json.dump(urls, file)

def get_new_urls(base_url, file_path):
    current_urls = fetch_current_zip_urls(base_url)
    stored_urls = load_stored_urls(file_path)

    # Find new or updated URLs
    new_urls = [url for url in current_urls if url not in stored_urls]

    # Update the stored URLs file
    save_urls(file_path, current_urls)

    return new_urls

# Example usage
base_url = 'http://download.cms.gov/nppes/NPI_Files.html'  # Replace with the actual base URL
file_path = r'{YOUR_DIRECTORY}stored_urls.json'  # Path to the file where URLs are stored
new_urls = get_new_urls(base_url, file_path)
print("New or Updated URLs:", new_urls)

