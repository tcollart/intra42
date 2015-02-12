from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('apps.core.urls', namespace='core', app_name='apps.core')),
    url(r'^tickets/', include('apps.tickets.urls', namespace='tickets', app_name='apps.tickets')),
    url(r'^forum/', include('apps.forum.urls', namespace='forum', app_name='apps.forum')),
    url(r'^admin/', include('apps.admincustom.urls', namespace='admincustom', app_name='apps.admincustom')),
    url(r'^djangoadmin/', include(admin.site.urls)),
)
