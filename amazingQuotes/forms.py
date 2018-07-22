from django import forms
from .models import ContactRequests


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequests
        fields = ['name','email','phoneno','message']


