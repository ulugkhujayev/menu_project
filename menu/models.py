from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    order = models.IntegerField(default=0)
    menu_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["menu_name", "order"]
        unique_together = ("menu_name", "order")

    def __str__(self):
        return f"{self.menu_name} - {self.name}"

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def clean(self):
        if not self.url and not self.named_url:
            raise ValidationError("Either URL or Named URL must be provided.")
        if self.url and self.named_url:
            raise ValidationError("Only one of URL or Named URL should be provided.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
