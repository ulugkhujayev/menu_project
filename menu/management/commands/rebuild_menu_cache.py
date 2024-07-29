from django.core.management.base import BaseCommand
from menu.utils import rebuild_menu_cache


class Command(BaseCommand):
    help = "Rebuilds the menu cache"

    def handle(self, *args, **options):
        rebuild_menu_cache()
        self.stdout.write(self.style.SUCCESS("Successfully rebuilt menu cache"))
