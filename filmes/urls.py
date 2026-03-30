from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes),           
    path('assistidos/', views.filmes_assistidos), 
]