
from django.contrib import admin
from app import views
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
