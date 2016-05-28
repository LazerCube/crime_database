from django.conf.urls import include, url
from . import views

app_name = 'management'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
]
