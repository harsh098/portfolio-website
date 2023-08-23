from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404
from .models import Project, CV
from .hashnode import getBlogs
from django.http import HttpResponse
import os


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

def downloadcv(request):
    cv = CV.objects.order_by('-created_at').first()
    cvURL = cv.cv.path
    if not os.path.exists(cvURL):
        raise Http404("PDF file not found.")
    
    # Open the PDF file in binary mode for reading
    with open(cvURL, 'rb') as pdf_file:
        # Create an HTTP response with PDF content type
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        
        # Set the Content-Disposition header to trigger download
        response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
        
        return response