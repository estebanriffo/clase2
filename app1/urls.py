from django.urls import path
from app1 import views

urlpatterns = [
    path('inicio/', views.index),
    path('nombre/', views.nombre),
]
