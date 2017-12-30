from django.conf.urls import include, url
from django.contrib import admin

from pdf_create import urls as pdf_create_urls


urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^summernote/', include('django_summernote.urls')),
        url(r'^', include(pdf_create_urls)),
]
