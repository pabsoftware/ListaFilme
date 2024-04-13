from django.urls import path
from . import views

urlpatterns = [
    path('categoria/novo/', views.cad_Categoria, name='cad_categoria'),
    path('filme/novo/', views.cad_filmes, name='cad_filmes'),
]