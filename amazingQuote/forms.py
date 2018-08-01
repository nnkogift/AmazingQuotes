from django import forms
from .models import ContactRequests, Order,EventRegistration


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequests
        fields = ['name','email','phoneno','message']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'name', 'email', 'phone_no']


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model= EventRegistration
        fields = ['name_of_registrar', 'email_of_registrar', 'phone_no']

