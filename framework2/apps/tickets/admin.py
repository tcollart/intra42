from django.contrib import admin

from .models import Ticket, TicketAnswer
# Register your models here.

admin.site.register(Ticket)
admin.site.register(TicketAnswer)
