from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import user_passes_test
from django.views.generic import RedirectView

from app.views import *


urlpatterns = patterns('', url(r'^$', Index.as_view(), name='home'),
                       url(r'^contact/$', Contact.as_view(), name='contact'),
                       url(r'^signup/$', SignUp.as_view(), name='signup'),
                       url(r'^signin/$', 'app.views.signin', {'template_name': 'signin.html'}, name='signin'),
                       url(r'^signout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='signout'),

                       url(r'^admin/$', RedirectView.as_view(url=reverse_lazy('AdminUsers')), name='AdminDefault'),

                       url(r'^admin/user/$', user_passes_test(lambda u: u.is_staff, login_url='/',
                                                              redirect_field_name='')(UsersList.as_view()), name='AdminUsers'),
                       url(r'^admin/user/create/$', user_passes_test(lambda u: u.is_staff, login_url='/',
                                                                     redirect_field_name='')(UserCreation.as_view()), name='AdminUserCreation'),
                       url(r'^admin/user/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff, login_url='/',
                                                              redirect_field_name='')(UserDetails.as_view()), name='AdminUsersDetails'),
                       url(r'^admin/user/delete/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff, login_url='/',
                                                              redirect_field_name='')(UserDeletion.as_view()), name='AdminUserDelete'),

                       url(r'^djangoadmin/', include(admin.site.urls)),
)
