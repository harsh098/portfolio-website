from django.shortcuts import render, redirect
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404
from .models import Message, Experience, ContactInfo
from .models import Project, CV
from .hashnode import getBlogs
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
import os


# Create your views here.
@cache_page(60 * 5)
def serve(request):
    try:
        projects = Project.objects.all().order_by('priority')[:10]
        exps = Experience.objects.all().order_by('-date_start')
        context = {
            "projects" : projects,
            "blogs" : getBlogs(), 
            "experience": exps,
            "contactInfo" : ContactInfo.objects.first(),
        }
        return render(request, 'index.html', context=context)
    except TemplateDoesNotExist:
        raise Http404("404 : Page Not Found")

@cache_page(60 * 5)
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


def contact_view(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Message instance and save it to the database
        new_message = Message(name=name, email=email, subject=subject, message=message)
        new_message.save()

        return redirect('contact')  # Redirect to a success page after submission
    
    return render(request, 'contact.html')  # Render the form template for GET requests
