from django.conf.urls import include, url
from . import views

app_name = 'management'
urlpatterns = [
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/student/(?P<student>[-\w]+)/$', views.student, name='student'),
    url(r'^home/$', views.home, name='home'),
]
