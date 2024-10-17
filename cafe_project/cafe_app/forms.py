from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class PhoneNumberAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Phone Number', max_length=15)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isdigit():
            raise ValidationError('Enter a valid phone number.')
        return username
