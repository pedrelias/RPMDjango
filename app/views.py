from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.views import View
from app.views import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')