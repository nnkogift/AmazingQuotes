from django import forms
from .models import ContactRequests, Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequests
        fields = ['name','email','phoneno','message']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'name', 'email', 'phone_no']


