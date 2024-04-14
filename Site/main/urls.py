from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path("", views.about, name="about"),
    path("about", views.about, name="about"),
    path("projects", ProjectListView.as_view(), name="projects"),
    path("education", EducationListView.as_view(), name="education")
]