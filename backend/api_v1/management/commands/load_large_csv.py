import os

from django.core.management.base import BaseCommand

from .get_download import RAW_DATA_DIR
from .shared_functions import KEYS, pg_load_table


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "load npi file"

    def add_arguments(self, parser):
        # required named args
        parser.add_argument("file", type=str, help='file name')
        # optional args
        parser.add_argument(
            "--sample",
            action="store_true",
            help="load sample npi data",
        )

    def handle(self, *args, **options):
        file = options.get("file")
        full_path = os.path.join(RAW_DATA_DIR, file)
        self.stdout.write("Starting load npi file")
        pg_load_table(full_path)
