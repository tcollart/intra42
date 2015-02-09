from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', Portal.as_view(), name='AdminPortal'),

    url(r'^user/$', UsersList.as_view(), name='AdminUsers'),
    url(r'^user/create/$', UserCreation.as_view(), name='AdminUserCreation'),
    url(r'^user/(?P<pk>\d+)/$', UserDetails.as_view(), name='AdminUsersDetails'),

    url(r'^forum/$', ForumList.as_view(), name='AdminForum'),
    url(r'^forum/create/childcategory/$', CategoryCreation.as_view(), name='AdminChildcategoryCreation'),
    url(r'^forum/create/category/$', CategoryCreation.as_view(), name='AdminCategoryCreation'),
    url(r'^forum/(?P<pk>\d+)/$', ForumDetails.as_view(), name='AdminForumDetails'),

    url(r'^tickets/$', TicketList.as_view(), name='AdminTickets'),
    url(r'^tickets/(?P<pk>\d+)/$', TicketDetails.as_view(), name='AdminTicketsDetails'),


)

