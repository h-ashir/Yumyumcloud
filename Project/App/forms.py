from django import forms
from App.models import Contact_Detail

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Detail
        fields = [
            'name', 'mobile_number', 'email', 'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-field', 'id': 'input-field', 'placeholder': 'Type Your Name', 'required': True}),
            'mobile_number': forms.TextInput(attrs={'class': 'mobile-number-field','type': 'tel' , 'id': 'input-field', 'placeholder': '+91 1234567890', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'email-field','type': 'email' , 'id': 'input-field', 'placeholder': 'example@gmail.com', 'required': True}),
            'message': forms.TextInput(attrs={'class': 'message-field', 'id': 'input-field', 'placeholder': 'Type your message', 'required': True}),
        }
