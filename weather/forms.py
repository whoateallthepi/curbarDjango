from django import forms
from .models import Reading

class SearchReadingForm(forms.Form):
    station = forms.IntegerField()
    date_from = forms.DateField()
    date_to = forms.DateField()
