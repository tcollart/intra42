from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView


from .forms import ContactForm, UpdateUserForm


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
    else:
        return login(request, **kwargs)


class SignUp(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/signin/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(SignUp, self).get(request, *args, **kwargs)


class UsersList(ListView):
    template_name = 'users.html'
    model = User


class UserCreation(CreateView):
    model = User
    template_name = "creation.html"
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'password']
    success_url = "/admin/user/"


class UserDetails(UpdateView):
    model = User
    template_name = "details.html"
    success_url = "/admin/user/"
    form_class = UpdateUserForm

    def form_valid(self, form):
        clean = form.cleaned_data
        new_password = clean.get('new_password')
        if new_password:
            form.instance.set_password(new_password)
        return super(UserDetails, self).form_valid(form)


class UserDeletion(DeleteView):
    model = User
    template_name = "user_confirm_delete.html"
    success_url = "/admin/user/"
