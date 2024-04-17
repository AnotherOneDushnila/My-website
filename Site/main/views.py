from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .form import *





class ProjectListView(ListView):
    model =  Project
    template_name = "projects.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        project = Project.objects.all()
        context["project"] = project
        return context
    

class EducationListView(ListView):
    model = Education
    template_name = "education.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        education = Education.objects.all()
        context["education"] = education
        return context
    

class ContactsListView(ListView):
    model = Contacts
    template_name = "contacts.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        context['message'] = Messages()
        return context
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit = False)
                message.flag = 'Ready to send'
                message.save()

        self.object_list = self.get_queryset()
        context = super().get_context_data(object_list = self.object_list, form = MessageForm())
        context['message'] = Messages()
        
        return render(request, "mysite/contacts_list.html", context = context)
    
def about(request):
    return render(request, "main/about.html")