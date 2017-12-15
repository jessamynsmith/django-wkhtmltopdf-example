from django.conf.urls import url

from pdf_create import views as pdf_create_views


urlpatterns = [
    url(r'^$', pdf_create_views.PdfCreateView.as_view(), name='pdf_create'),
]
