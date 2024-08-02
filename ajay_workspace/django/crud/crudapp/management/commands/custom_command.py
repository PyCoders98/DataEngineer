from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "custom command Demonstration"

    def add_arguments(self, parser):
        parser.add_argument()