from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
            self.stdout.write(
                self.style.SUCCESS('HELLO WORLD')
            )