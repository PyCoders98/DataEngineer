from django import forms
from .models import *


class DetailForms(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
