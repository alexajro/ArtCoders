from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.shortcuts import render
from datetime import datetime
from . import views

# Create your views here.
# pages/views.py
def home(request):
    return render(request,'index.html')
def second(request):
    return render(request,"templates/second.html", None)
def bienvenidas(request):
    return render(request,"templates/bienvenidas.html", None)
