from django.conf.urls import patterns, include, url
from apps.students.views import StudentsList, StudentDetails

urlpatterns = patterns('apps.students.views',
    url(r'^$', StudentsList.as_view(), name='studentsindex'),
    url(r'^(?P<slug>\w+)/$', StudentDetails.as_view(), name='studentdetail'),
    # url(r'^(?P<category_slug>\w+)/$', 'category_view', name='forumcategories'),
    # url(r'^(?P<category_slug>\w+)/(?P<childcategory_slug>\w+)/new/$', StudentsList.as_view(), name='forumindex'),

)

