from django import forms
from .models import Requests




class FormClass(forms.ModelForm):
    class Meta:
        model=Requests
        exclude = ['deadline','letter']
