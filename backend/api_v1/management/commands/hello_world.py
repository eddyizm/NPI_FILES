from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    '''doc link https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/'''
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("HELLO WORLD"))
