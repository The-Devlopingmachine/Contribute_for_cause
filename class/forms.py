from django import forms
from django.forms import fields
from .models import Entry

class CauseForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'Company_name',
            'discreption',
            'deatils',
            'last_date',
            'application_url',
            'published_date',
        ]