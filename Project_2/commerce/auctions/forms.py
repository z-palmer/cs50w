from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description',
                  'category', 'image', 'user')
        widgets = {'user': forms.HiddenInput()}
