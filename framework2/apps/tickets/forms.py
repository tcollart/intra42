from django import forms


class AnswerForm(forms.Form):
    ticketanswer = forms.CharField(widget=forms.Textarea, max_length=1024, label="Your message")