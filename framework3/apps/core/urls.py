from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .views import *

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='home'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^signup/$', CreateView.as_view(template_name='signup.html', form_class=UserCreationForm, success_url='/signin/')),
    url(r'^signin/$', 'apps.core.views.signin', {'template_name': 'signin.html'}, name='signin'),
    url(r'^signout/$', 'apps.core.views.signout', name='signout'),
    # url(r'^admin/$', Admin.as_view(), name='home'),
)
