from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "url", "named_url", "parent", "order", "menu_name"]

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get("url")
        named_url = cleaned_data.get("named_url")

        if url and named_url:
            raise forms.ValidationError(
                "Only one of URL or Named URL should be provided."
            )
        if not url and not named_url:
            raise forms.ValidationError("Either URL or Named URL must be provided.")

        return cleaned_data
