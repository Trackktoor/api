from django import forms
from .models import URL

class NameForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ('full_url',)