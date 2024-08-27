from django.urls import path
from app2 import views

urlpatterns = [
    path('index/', views.index),
    path('chistemalo/', views.chistemalo),
    path('queso/', views.queso)
]