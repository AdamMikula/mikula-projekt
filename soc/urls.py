from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='soc'),
    path('tema/', views.nova_tema, name='tema'),
]