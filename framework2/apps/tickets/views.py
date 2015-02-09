from datetime import datetime

from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.contrib import messages

from .models import Ticket, TicketAnswer
from .forms import AnswerForm


class TicketList(ListView):
    template_name = 'usertickets.html'

    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(TicketList, self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.filter(author=self.request.user)
        return context


class TicketCreate(CreateView):
    template_name = 'ticketcreation.html'
    success_url = '/tickets/'
    model = Ticket
    fields = ['title', 'message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(TicketCreate, self).form_valid(form)


def details(request, ticket_id):

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            messages.success(request, "Answer posted")
            answer = TicketAnswer(author=request.user,
                                  message=form.cleaned_data['ticketanswer'],
                                  creation_date=datetime.now(),
                                  ticket_related=Ticket.objects.get(pk=ticket_id))
            answer.save()
        else:
            ticket = Ticket.objects.get(pk=ticket_id)
            ticket.resolved = False
            ticket.save()
    else:
        form = AnswerForm()

    ticket = Ticket.objects.get(pk=ticket_id)
    ticket_answers = TicketAnswer.objects.filter(ticket_related=ticket)

    return render(request, 'ticketdetails.html', {'ticket': ticket, 'ticketanswers': ticket_answers, 'form': form})

'''
author = models.ForeignKey(User, related_name='TicketAnswerAuthor')
    message = models.TextField(max_length=10000, blank=False)
    creation_date = models.DateField(default=datetime.now)

    ticket_related = models.ForeignKey(Ticket, related_name='TicketAnswer')
'''