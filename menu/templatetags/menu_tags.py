from django import template
from django.urls import resolve, Resolver404
from menu.models import MenuItem
from django.core.cache import cache

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path

    cache_key = f"menu_{menu_name}_{current_path}"
    cached_menu = cache.get(cache_key)
    if cached_menu:
        return cached_menu

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related("parent")

    def build_menu(parent=None, path=None):
        items = [item for item in menu_items if item.parent == parent]
        tree = []
        for item in items:
            active = item.get_absolute_url() == current_path
            expanded = path and item.get_absolute_url() in path
            node = {
                "item": item,
                "is_active": active,
                "is_expanded": expanded,
                "children": build_menu(item, path if expanded else None),
            }
            tree.append(node)
        return tree

    try:
        current_url_name = resolve(current_path).url_name
        path = []
        for item in menu_items:
            if item.named_url == current_url_name or item.url == current_path:
                while item:
                    path.append(item.get_absolute_url())
                    item = item.parent
                break
    except Resolver404:
        path = None

    menu = build_menu(path=path)
    cache.set(cache_key, menu, 60 * 15)  # Cache for 15 minutes
    return menu
