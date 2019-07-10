from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
import blog
# Create your views here.

def index(request):
    return render(request,"blog/index.html")