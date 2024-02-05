import os

from django.core.management.base import BaseCommand

from .get_download import RAW_DATA_DIR
from .shared_functions import KEYS, pg_load_table


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "loads npi file, passing file name as an argument\nfile must be in the RAW_DATA_DIR directory."

    def add_arguments(self, parser):
        # required named args
        parser.add_argument("file", type=str, help='file name')

    def handle(self, *args, **options):
        file = options.get("file")
        full_path = os.path.join(RAW_DATA_DIR, file)
        self.stdout.write(f"Starting load npi file, filename: {file}")
        pg_load_table(full_path)
