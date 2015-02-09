from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from settings import TICKETS_MANAGER_ID


class Ticket(models.Model):
    author = models.ForeignKey(User, related_name='TicketAuthor', default=None)
    title = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=10000, blank=False)
    creation_date = models.DateField(default=datetime.now)
    assigned_to = models.ForeignKey(User, related_name='TicketAssignedTo',
                                    help_text="Assign the ticket to an admin",
                                    default=TICKETS_MANAGER_ID, null=False, blank=False)
    resolved = models.BooleanField(default=False)
    validated_by = models.ForeignKey(User, related_name='TicketValidatedBy', default=None, null=True, blank=True)
    validated_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class TicketAnswer(models.Model):
    author = models.ForeignKey(User, related_name='TicketAnswerAuthor')
    message = models.TextField(max_length=10000, blank=False)
    creation_date = models.DateField(default=datetime.now)

    ticket_related = models.ForeignKey(Ticket, related_name='TicketAnswer')