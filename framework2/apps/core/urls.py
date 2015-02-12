from django.conf.urls import patterns, include, url
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .views import *

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='home'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^signup/$', user_passes_test(lambda u: not u.is_authenticated(), login_url='/',
                                       redirect_field_name='')(CreateView.as_view(template_name='signup.html',
                                                                                  form_class=UserCreationForm,
                                                                                  success_url='/signin/'))),
    url(r'^signin/$', 'apps.core.views.signin', {'template_name': 'signin.html'}, name='signin'),
    url(r'^signout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='signout'),

    (r'^i18n/', include('django.conf.urls.i18n')),
)
