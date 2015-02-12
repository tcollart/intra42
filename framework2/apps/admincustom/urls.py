from django.conf.urls import patterns, include, url
from django.contrib.admin.views.decorators import user_passes_test

from .views import *

urlpatterns = patterns('',
    url(r'^$',                              user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(Portal.as_view()),name='AdminPortal'),
    url(r'^user/$',                         user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(UsersList.as_view()), name='AdminUsers'),
    url(r'^user/create/$',                  user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(UserCreation.as_view()), name='AdminUserCreation'),
    url(r'^user/(?P<pk>\d+)/$',             user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(UserDetails.as_view()), name='AdminUsersDetails'),
    url(r'^user/delete/(?P<pk>\d+)/$',      user_passes_test(lambda u: u.is_staff, login_url='/',
                                                              redirect_field_name='')(UserDeletion.as_view()), name='AdminUserDelete'),
    url(r'^forum/$',                        user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(ForumList.as_view()), name='AdminForum'),
    url(r'^forum/create/childcategory/$',   user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(CategoryCreation.as_view()), name='AdminChildcategoryCreation'),
    url(r'^forum/create/category/$',        user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(CategoryCreation.as_view()), name='AdminCategoryCreation'),
    url(r'^forum/(?P<pk>\d+)/$',            user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(ForumDetails.as_view()), name='AdminForumDetails'),
    url(r'^tickets/$',                      user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(TicketList.as_view()), name='AdminTickets'),
    url(r'^tickets/(?P<pk>\d+)/$',          user_passes_test(lambda u: u.is_staff, login_url='/',
                                                             redirect_field_name='')(TicketDetails.as_view()), name='AdminTicketsDetails'),
)