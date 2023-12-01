import os

import requests

from django.core.management.base import BaseCommand
from npi_api.settings import BASE_DIR
from api_v1.models import DownloadURL


# TODO dump extracted files to a archived location, eg, s3 bucket
TEMP_DIR = os.path.join(BASE_DIR, "tmp")


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
            _id = self.download_nppes_data_dissemination_zip_file(file)

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
            self.stdout.write(self.style.ERROR(f'Error downloading file:\n{err}'))
            return response.status_code

    def download_nppes_data_dissemination_zip_file(self, nppes_data: DownloadURL) -> int:
        """'download nppes data zip files. """
        # TODO Add zip extraction, delete zips and load flat files into db.
        url = nppes_data.url
        target_path = os.path.join(TEMP_DIR, nppes_data.file_name)
        self.stdout.write(f'downloading file: {nppes_data.file_name}')
        if self.download_file(url, target_path) == 200:
            # mark downloaded, and then process zip file
            # file = DownloadURL.objects.get(id=nppes_data.id)
            # file.downloaded = True
            # file.save()
            result = DownloadURL.objects.filter(id=nppes_data.id).update(downloaded=True)
            breakpoint()
            return nppes_data.id
