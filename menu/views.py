from django.views.generic import TemplateView
from .models import MenuItem


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.filter(menu_name="main", parent=None)
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.filter(menu_name="main", parent=None)
        return context
