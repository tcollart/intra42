from django.conf.urls import patterns, url

from apps.forum.views import CreateThread

urlpatterns = patterns('apps.forum.views',
    url(r'^$', 'global_view', name='forumindex'),
    url(r'^(?P<category_slug>\w+)/$', 'category_view', name='forumcategories'),
    url(r'^(?P<category_slug>\w+)/(?P<childcategory_slug>\w+)/$', 'childcategory_view', name='forumchildcategories'),
    url(r'^(?P<category_slug>\w+)/(?P<childcategory_slug>\w+)/(?P<thread_id>\d+)/$', 'thread_view', name='forumthread'),
    url(r'^(?P<category_slug>\w+)/(?P<childcategory_slug>\w+)/new/$', CreateThread.as_view(), name='forumindex'),

)

