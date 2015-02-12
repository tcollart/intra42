from django import forms


class ContactForm(forms.Form):
    login = forms.CharField(label='Login', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=100)
    cc_myself = forms.BooleanField(label='CC me', required=False)