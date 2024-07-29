from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import MenuItem
from .utils import clear_menu_cache


@receiver(post_save, sender=MenuItem)
@receiver(post_delete, sender=MenuItem)
def clear_cache_on_change(sender, **kwargs):
    clear_menu_cache()
