
from django.contrib import admin
from app import views
from app.views import *
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('f1/', f1_view, name='f1'),
    path('indy/', indy_view, name='indy'),
    path('nascar/', nascar_view, name='nascar'),
]

