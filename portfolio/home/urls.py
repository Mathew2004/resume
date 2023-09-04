from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name="Homepage"),
    path('about/', views.about, name="about"),
    path('allprojects/', views.projects, name="Projects"),
    path('contact/', views.contact, name="Contact"),
    
]