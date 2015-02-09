from django.conf.urls import patterns, include, url
from .views import TicketList, TicketCreate


urlpatterns = patterns('apps.tickets.views',
    url(r'^$', TicketList.as_view(), name='forumindex'),
    url(r'^(?P<ticket_id>\d+)/$', 'details', name='ticketdetails'),
    url(r'^new/$', TicketCreate.as_view(), name='forumindex'),
)

