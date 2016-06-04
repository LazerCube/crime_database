from django.conf.urls import include, url
from . import views

app_name = 'management'
urlpatterns = [
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/student/add/$', views.add, name='add'),
    url(r'^admin/student/(?P<student>[-\w]+)/$', views.student, name='student'),
    url(r'^admin/student/(?P<student>[-\w]+)/delete$', views.delete, name='delete'),
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
]
