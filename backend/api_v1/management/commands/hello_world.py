from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/"""

    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # required named args
        # parser.add_argument("poll_ids", nargs="+", type=int)

        # optional args
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete poll instead of closing it",
        )

    def handle(self, *args, **options):
        _delete = options["delete"]
        self.stdout.write(self.style.HTTP_INFO(f"delete option: {_delete}"))
        self.stdout.write(self.style.SUCCESS("HELLO WORLD"))
