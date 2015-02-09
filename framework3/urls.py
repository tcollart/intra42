from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('apps.core.urls', namespace='core', app_name='apps.core')),
    url(r'^tickets/', include('apps.tickets.urls', namespace='tickets', app_name='apps.tickets')),
    url(r'^forum/', include('apps.forum.urls', namespace='forum', app_name='apps.forum')),
    url(r'^myadmin/', include('apps.admincustom.urls', namespace='admincustom', app_name='apps.admincustom')),
    url(r'^users/', include('apps.students.urls', namespace='students', app_name='apps.students')),
    url(r'^admin/', include(admin.site.urls)),
)
