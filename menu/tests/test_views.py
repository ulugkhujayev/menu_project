from django.test import TestCase
from django.urls import reverse
from menu.models import MenuItem


class MenuViewsTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Home", url="/", menu_name="main")
        MenuItem.objects.create(name="About", url="/about/", menu_name="main")

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")
        self.assertContains(response, "About")

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")
        self.assertContains(response, "About")
