from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'),
    path('edicao/', views.edicao, name='edicao')
]
