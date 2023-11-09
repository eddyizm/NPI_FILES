import requests

def download_file(url, target_path):
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    with open(target_path, 'wb') as f:
        f.write(response.content)
    print("Download completed!")

def main():
    """Needs a way to change the URL every month. 'target_path' is the directory of your project"""
    url = 'https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_100923.zip'  # This URL will change every second Monday of the month.
    target_path = r'your_directory\file.zip'  #ake sure the file name is in the directory. Won't work without it. 

    download_file(url, target_path)

if __name__ == "__main__":
    main()

