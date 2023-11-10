from get_monthly_url import GetURL
import requests

def download_file(url, target_path):
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    with open(target_path, 'wb') as f:
        f.write(response.content)
    print("Download completed!")

def main():
    """Needs a way to change the URL every month. 'target_path' is the directory of your project"""
    class_object = GetURL()
    url = class_object.get_monthly_url()
    target_path = r'C:\Users\sghal\Desktop\Download_NPI"\test.zip'  #make sure the file name is in the directory. Won't work without it. 

    download_file(url, target_path)

if __name__ == "__main__":
    main()

