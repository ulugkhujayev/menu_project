from django.test import TestCase
from django.core.exceptions import ValidationError
from menu.models import MenuItem


class MenuItemModelTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(name="Home", url="/", menu_name="main")

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.name, "Home")
        self.assertEqual(self.menu_item.url, "/")
        self.assertEqual(self.menu_item.menu_name, "main")

    def test_menu_item_str_representation(self):
        self.assertEqual(str(self.menu_item), "main - Home")

    def test_get_absolute_url(self):
        self.assertEqual(self.menu_item.get_absolute_url(), "/")

    def test_url_or_named_url_required(self):
        with self.assertRaises(ValidationError):
            MenuItem.objects.create(name="Invalid", menu_name="main")

    def test_url_and_named_url_mutually_exclusive(self):
        with self.assertRaises(ValidationError):
            MenuItem.objects.create(
                name="Invalid", url="/invalid/", named_url="invalid", menu_name="main"
            )
