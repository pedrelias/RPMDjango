
from django.contrib import admin
from app import views
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('f1/', TemplateView.as_view(template_name='f1/f1.html'), name='f1'),
    path('nascar/', TemplateView.as_view(template_name='nascar/nascar.html'), name='nascar'),
    path('indy/', TemplateView.as_view(template_name='indy/indy.html'), name='indy'),
]

