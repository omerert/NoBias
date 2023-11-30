from django import forms
from .models import SubmittedLink

class LinkForm(forms.ModelForm):
    class Meta:
        model = SubmittedLink
        fields = ['link']