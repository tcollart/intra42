__author__ = 'tcollart'

from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):

    login = forms.CharField(label='Login', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=100)
    cc_myself = forms.BooleanField(label='CC me', required=False)


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')

    new_password = forms.CharField(required=False, widget=forms.widgets.PasswordInput)