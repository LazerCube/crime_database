from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('accounts.urls')),
    url(r'^', include('management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
