from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def HomepageView(request):
    return render(request, 'index.html', context={})


def LoginView(request):
    return render(request, 'login.html', context={})


def RegisterView(request):
    return render(request, 'register.html', context={})
