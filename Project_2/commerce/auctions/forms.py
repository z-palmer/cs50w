from django import forms
from .models import Listing


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Listing
        fields = ('title', 'image')
