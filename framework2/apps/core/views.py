from django.conf import settings
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import translation
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView

from .forms import ContactForm


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        language = request.GET.get("language")
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language
        return render(request, self.template_name)


class Contact(FormView):
    template_name = 'contact.html'
    success_url = '/contact/'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        self.initial = {'login': request.user, 'email': request.user.email} if request.user.is_authenticated() else {}
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        subject = form.cleaned_data['login']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = settings.CONTACT_EMAIL

        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)

        return super(Contact, self).form_valid(form)


def signin(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return login(request, **kwargs)


class Admin(ListView):
    template_name = 'admin.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(Admin, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context