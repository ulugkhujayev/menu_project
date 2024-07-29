from django.core.cache import cache
from .models import MenuItem


def clear_menu_cache():
    cache.clear()


def rebuild_menu_cache():
    clear_menu_cache()
    menus = MenuItem.objects.values("menu_name").distinct()
    for menu in menus:
        MenuItem.objects.filter(menu_name=menu["menu_name"])
