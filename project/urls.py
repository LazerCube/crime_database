from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('accounts.urls')),
    url(r'^', include('management.urls')),
]
