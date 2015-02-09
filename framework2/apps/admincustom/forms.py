from django.contrib.auth.models import User
from django import forms

from apps.tickets.models import Ticket


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')

    new_password = forms.CharField(required=False, widget=forms.widgets.PasswordInput)


class TicketAdminAnswer(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['assigned_to', 'resolved']

    ticketanswer = forms.CharField(widget=forms.Textarea, max_length=1024, label="Your message", required=False)