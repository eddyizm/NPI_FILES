import os

from django.core.management.base import BaseCommand

from .get_download import TEMP_DIR
from .shared_functions import KEYS, pg_load_table


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "seed sample npi file"

    def add_arguments(self, parser):
        # required named args
        pass
        # # optional args
        # parser.add_argument(
        #     "--sample",
        #     action="store_true",
        #     help="load sample npi data",
        # )

    def handle(self, *args, **options):
        full_path = os.path.join(TEMP_DIR, 'sample_np-data_pfile.csv')
        self.stdout.write("Loading sample_np-data_pfile.csv file")
        pg_load_table(full_path)
