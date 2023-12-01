import os

import requests
import zipfile

from django.core.management.base import BaseCommand
from npi_api.settings import BASE_DIR
from api_v1.models import DownloadURL


# TODO dump extracted files to a archived location, eg, s3 bucket
TEMP_DIR = os.path.join(BASE_DIR, "tmp")
RAW_DATA_DIR = os.path.join(
    BASE_DIR, "raw_data"
)  # this should map to a container volume when deployed.


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
        self.stdout.write("Starting get download")
        new_files = self.get_npi_files()
        for file in new_files:
            # self.stdout.write(self.style.HTTP_INFO(file))
            zip_path = self.download_nppes_data_dissemination_zip_file(file)
            self.stdout.write(f"Extracting zip at path: {zip_path}")
            self.extract_file_and_load_to_db(file, zip_path)

    def extract_file_and_load_to_db(self, nppes_data: DownloadURL, zip_path: str):
        """extract zip to raw data directory"""
        # full_path = os.path.join(RAW_DATA_DIR, nppes_data.file_name)
        self.stdout.write(f"Extracting text file to path: {RAW_DATA_DIR}")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            for zip in zip_ref.namelist():
                zip_ref.extract(member=zip, path=RAW_DATA_DIR)
                DownloadURL.objects.filter(id=nppes_data.id).update(
                    text_file_name=zip, text_file_path=RAW_DATA_DIR
                )
                self.stdout.write(self.style.SUCCESS("Text file extracted Successfully! and DB UPDATED!"))

    def get_npi_files(self) -> list[DownloadURL]:
        files = DownloadURL.objects.filter(downloaded=False)
        self.stdout.write(self.style.HTTP_INFO(f"files to download: {len(files)}"))
        return files

    def download_file(self, url: str, target_path: str) -> int:
        # TODO implement check to make we the file doesn't already exists or we already didn't DL and dumped it into the db.
        try:
            response = requests.get(url, allow_redirects=True)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

            with open(target_path, "wb") as f:
                f.write(response.content)
            self.stdout.write(self.style.SUCCESS("Download completed!"))
            return response.status_code
        except requests.RequestException as err:
            self.stdout.write(self.style.ERROR(f"Error downloading file:\n{err}"))
            return response.status_code

    def download_nppes_data_dissemination_zip_file(
        self, nppes_data: DownloadURL
    ) -> str:
        """'download nppes data zip files."""
        # TODO Add zip extraction, delete zips and load flat files into db.
        url = nppes_data.url
        target_path = os.path.join(TEMP_DIR, nppes_data.file_name)
        self.stdout.write(f"downloading file: {nppes_data.file_name}")
        if self.download_file(url, target_path) == 200:
            assert 1 == DownloadURL.objects.filter(id=nppes_data.id).update(
                downloaded=True
            )
            return target_path
