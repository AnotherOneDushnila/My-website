from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path("", views.about, name="about"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("education", views.education, name="education")
]