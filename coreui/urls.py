from django.urls import path
from . import views
urlpatterns = [
    path('', views.serve, name='homepage'),
    path('download_cv/', views.downloadcv, name='servepdf'),
    path('contact/', views.contact_view, name='contact'),
    path('message_sent/<str:name>/<str:email>', views.success_page, name='success')
]