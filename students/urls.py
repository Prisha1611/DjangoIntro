from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('classes/', views.classes)
]