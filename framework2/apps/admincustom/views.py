from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from .forms import UpdateUserForm, TicketAdminAnswer
from apps.forum.models import BaseCategory, Category, ChildCategory
from apps.tickets.models import Ticket, TicketAnswer


class Portal(TemplateView):
    template_name = 'portal.html'


class UsersList(ListView):
    template_name = 'users.html'
    model = User


class UserCreation(CreateView):
    model = User
    template_name = "creation.html"
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'password']
    success_url = "/myadmin/user/"


class UserDetails(UpdateView):
    model = User
    template_name = "details.html"
    success_url = "/myadmin/user/"
    form_class = UpdateUserForm

    def form_valid(self, form):
        clean = form.cleaned_data
        new_password = clean.get('new_password')
        if new_password:
            form.instance.set_password(new_password)
        return super(UserDetails, self).form_valid(form)


class ForumList(ListView):
    model = BaseCategory
    template_name = "forum.html"


class ChildCategoryCreation(CreateView):
    model = ChildCategory
    template_name = "creation.html"
    success_url = "/myadmin/forum/"


class CategoryCreation(CreateView):
    model = Category
    template_name = "creation.html"
    success_url = "/myadmin/forum/"


class ForumDetails(UpdateView):
    model = BaseCategory
    template_name = "details.html"
    success_url = "/myadmin/forum/"


class TicketList(ListView):
    model = Ticket
    template_name = "tickets.html"


class TicketDetails(UpdateView):
    model = Ticket
    form_class = TicketAdminAnswer
    template_name = "ticketupdatedetails.html"

    def get_context_data(self, **kwargs):
        context = super(TicketDetails, self).get_context_data(**kwargs)
        context['answers'] = TicketAnswer.objects.filter(ticket_related=self.object)
        return context

    def get_success_url(self):
        return ""

    def form_valid(self, form):
        form_changed = False
        if 'resolved' in form.cleaned_data and form.cleaned_data['resolved'] != form.instance.resolved:
            form.instance.resolved = form.cleaned_data['resolved']
            form_changed = True
        if 'assigned_to' in form.cleaned_data and form.cleaned_data['assigned_to'] != form.instance.assigned_to:
            form.instance.assigned_to = User.objects.get(pk=form.cleaned_data['assigned_to'])
            form_changed = True
        if form_changed:
            form.save()
        if 'ticketanswer' in form.cleaned_data and form.cleaned_data['ticketanswer']:
            messages.success(self.request, "Answer posted")
            answer = TicketAnswer(author=self.request.user,
                                  message=form.cleaned_data['ticketanswer'],
                                  creation_date=datetime.now(),
                                  ticket_related=self.get_object())
            answer.save()
        return super(TicketDetails, self).form_valid(form)