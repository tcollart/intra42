import ldap3

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView

from apps.admincustom.models import MyLogEntry
from .forms import ContactForm


class Index(TemplateView):
    template_name = 'index.html'


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
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        user_filter = User.objects.filter(username=username)
        user_obj = user_filter[0] if len(user_filter) else None
        if user and user_obj and user_obj.is_active:
            log_entry = MyLogEntry(user=User.objects.get(pk=user.id),
                                   message="logged in.")
            log_entry.save()
        elif username and password:
            pool = request.POST.get('pool', '')
            year = request.POST.get('year', '')
            s = ldap3.Server("ldaps://ldap.42.fr", port=636, use_ssl=True, get_info=ldap3.GET_ALL_INFO)
            try:
                c = ldap3.Connection(s,
                                     authentication=ldap3.AUTH_SIMPLE,
                                     check_names=True,
                                     auto_bind=True,
                                     user="uid="+username+",ou="+pool+",ou="+year+",ou=paris,ou=people,dc=42,dc=fr",
                                     password=password)
            except ldap3.LDAPBindError:
                return login(request, **kwargs)
            if c.result['description'] == 'success':
                user_obj = User.objects.get(username=username)
                user_obj.set_password(password)
                user_obj.is_active = True
                user_obj.save()
    return login(request, **kwargs)


def signout(request):
    if request.user.is_authenticated():
        log_entry = MyLogEntry(user=User.objects.get(pk=request.user.id),
                               message="logged out.")
        log_entry.save()
        logout(request)
    return HttpResponseRedirect('/')


class Admin(ListView):
    template_name = 'admin.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(Admin, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
