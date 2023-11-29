from django.core.management.base import BaseCommand

from api_v1.models import DownloadURL

import requests

BASE_URL = "https://download.cms.gov"
BASE_PATH = "nppes"
INFO_URL = f"{BASE_URL}/{BASE_PATH}/NPI_Files.html"


def download_file(url, target_path):
    # TODO implement check to make we the file doesn't already exists or we already didn't DL and dumped it into the db.
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    with open(target_path, "wb") as f:
        f.write(response.content)
    print("Download completed!")


def download_deactivated_npi_report_zip():
    """'target_path' is the directory of your project"""
    # TODO Needs a way to change the URL every month.
    # This URL will change every second Monday of the month.
    file_name = "NPPES_Deactivated_NPI_Report_100923.zip"  # filenamne to be generated dynamically from scrape
    url = f"{BASE_URL}/{BASE_PATH}/{file_name}"
    target_path = f"tmp/{file_name}"

    download_file(url, target_path)


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # required named args
        # parser.add_argument("poll_ids", nargs="+", type=int)

        # optional args
        parser.add_argument(
            "-d",
            "--download",
            action="store_true",
            help="Download files",
        )

    def handle(self, *args, **options):
        # self.stdout.write(self.style.HTTP_INFO(f"poll id: {arg1}"))
        self.stdout.write(self.style.SUCCESS("Starting get download"))
        new_files = self.get_npi_files()
        for file in new_files:
            self.stdout.write(self.style.HTTP_INFO(file))

    def get_npi_files(self) -> list[DownloadURL]:
        files = DownloadURL.objects.filter(downloaded=False)
        self.stdout.write(self.style.HTTP_INFO(f"files to download: {len(files)}"))
        return files
