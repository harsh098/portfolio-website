from django.urls import path
from . import views
urlpatterns = [
    path('', views.serve, name='homepage'),
    path('download_cv/', views.downloadcv, name='servepdf'),
    path('contact/', views.contact_view, name='contact')
]