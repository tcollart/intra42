from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import TicketList, TicketCreate, details


urlpatterns = patterns('apps.tickets.views',
    url(r'^$',                      login_required(login_url='/', redirect_field_name='')(TicketList.as_view()), name='forumindex'),
    url(r'^(?P<ticket_id>\d+)/$',   login_required(login_url='/', redirect_field_name='')(details), name='ticketdetails'),
    url(r'^new/$',                  login_required(login_url='/', redirect_field_name='')(TicketCreate.as_view()), name='forumindex'),
)

