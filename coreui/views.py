from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404
from .models import Project
from .hashnode import getBlogs

# Create your views here.
def serve(request):
    try:
        projects = Project.objects.all().order_by('priority')[:10]
        context = {
            "projects" : projects,
            "blogs" : getBlogs(), 
        }
        return render(request, 'index.html', context=context)
    except TemplateDoesNotExist:
        raise Http404("404 : Page Not Found")
