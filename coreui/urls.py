from django.urls import path
from . import views
urlpatterns = [
    path('', views.serve, name='homepage'),
]