from django.shortcuts import render
from .models import Project
from blog import views
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects':projects})

