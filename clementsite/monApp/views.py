from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here


from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
##from .models import client

def index(request):
   return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def brokenpage(request):
    return render(request, 'brokenpage.html')

def nothing(request):
    return render(request, 'monApp/nothing.html')

def useless_page(request):
	return render(request, 'useless_page.html')

