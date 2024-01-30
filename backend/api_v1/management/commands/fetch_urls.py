import requests
import re
import urllib.parse

from django.core.management.base import BaseCommand, CommandError
from api_v1.models import DownloadURL
from api_v1.schemas.download_url import DownloadURLIn

NPI_FILES_URL = "http://download.cms.gov/nppes/NPI_Files.html"


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "Download url and parse out zip files"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.get_new_urls(NPI_FILES_URL)

    def fetch_current_zip_urls(self, base_url):
        response = requests.get(base_url)
        relative_urls = re.findall(
            r"href='(\./NPPES_Data_Dissemination_[^']*?\.zip)'", response.text
        )
        current_urls = [urllib.parse.urljoin(base_url, url) for url in relative_urls]
        return current_urls

    def map_urls_to_schema(self, current_urls):
        self.stdout.write(self.style.HTTP_INFO("Mapping urls to Schema..."))
        try:
            mapped_urls = []
            for url in current_urls:
                fname = url.replace("http://download.cms.gov/nppes/", "")
                mapped_urls.append(
                    DownloadURLIn(
                        file_name=fname, created_by="fetch_urls.py", url=url
                    ).dict()
                )
            return mapped_urls
        except Exception:
            raise CommandError("Error mapping urls")

    def save_urls(self, download_urls: list):
        self.stdout.write(
            self.style.HTTP_INFO("Saving urls in bulk create statement...")
        )
        DownloadURL.objects.bulk_create([DownloadURL(**item) for item in download_urls])

    def get_new_urls(self, base_url: str):
        self.stdout.write(self.style.HTTP_INFO("Checking URL for new data..."))
        current_urls = self.fetch_current_zip_urls(base_url)
        self.stdout.write(self.style.HTTP_INFO(f"Found {len(current_urls)} zip urls"))

        # Find new or updated URLs
        # TODO this needs to check the db or better yet, make the file name a unique field in the db, so inserts fail.
        urls = self.map_urls_to_schema(current_urls)

        self.save_urls(urls)
        self.stdout.write(self.style.SUCCESS("URLS loaded to database successfully"))
