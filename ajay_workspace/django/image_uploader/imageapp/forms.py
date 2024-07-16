from django import forms
from .models import *


class ProfileImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_image"]
