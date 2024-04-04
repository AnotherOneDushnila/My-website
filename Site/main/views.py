from django.shortcuts import render
from .models import *

# Create your views here.

def about(request):
    return render(request, "main/about.html")

def projects(request):
    return render(request, "main/projects.html", {"Project" : Project.objects.all()})

def education(request):
    return render(request, "main/education.html", {"Education" : Education.objects.all()})