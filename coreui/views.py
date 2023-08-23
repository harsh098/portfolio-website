from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404

# Create your views here.
def serve(request):
    try:
        return render(request, 'index.html')
    except TemplateDoesNotExist:
        raise Http404("404 : Page Not Found")

def fetchBlogs():
    pass