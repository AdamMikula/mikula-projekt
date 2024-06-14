from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='soc'),
    path('tema/', views.nova_tema, name='tema'),
    path('konzultant/<int:konzultant_id>/', views.konzultant_detail, name='konzultant_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('update-konzultacie/<int:pk>/', views.update_konzultacie, name='update_konzultacie'),
    path('statistiky/', views.statistiky, name='statistiky'),
]