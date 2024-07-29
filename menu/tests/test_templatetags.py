from django.test import TestCase, RequestFactory
from django.template import Context, Template
from menu.models import MenuItem


class MenuTagsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        MenuItem.objects.create(name="Home", url="/", menu_name="main")
        MenuItem.objects.create(name="About", url="/about/", menu_name="main")

    def test_draw_menu_tag(self):
        request = self.factory.get("/")
        out = Template("{% load menu_tags %}" "{% draw_menu 'main' %}").render(
            Context({"request": request})
        )
        self.assertIn("Home", out)
        self.assertIn("About", out)
        self.assertIn('class="active"', out)

    def test_draw_menu_tag_with_children(self):
        parent = MenuItem.objects.create(
            name="Parent", url="/parent/", menu_name="main"
        )
        MenuItem.objects.create(
            name="Child", url="/parent/child/", menu_name="main", parent=parent
        )

        request = self.factory.get("/parent/")
        out = Template("{% load menu_tags %}" "{% draw_menu 'main' %}").render(
            Context({"request": request})
        )
        self.assertIn("Parent", out)
        self.assertIn("Child", out)
        self.assertIn('class="active"', out)
        self.assertIn('class="expanded"', out)
