from django import forms
from .models import Listing, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description',
                  'category', 'image', 'user')
        widgets = {'user': forms.HiddenInput()}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'listing', 'user')

        widgets = {'user': forms.HiddenInput(), 'listing': forms.HiddenInput()}
