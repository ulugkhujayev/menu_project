from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ("name", "url", "named_url", "parent", "order", "menu_name")
    list_filter = ("menu_name",)
    search_fields = ("name", "url", "named_url")
    ordering = ("menu_name", "order")

    def get_changeform_initial_data(self, request):
        return {"menu_name": "main"}
