from django.conf.urls import include, url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^account/view$', views.account, name='view'),
    #url(r'^admin/(?P<account>[-\w]+)/view/$', views.student_account, name='student_account'),
    url(r'^admin/account/(?P<account>[-\w]+)/view/$', views.student_account, name='student_account'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
]
