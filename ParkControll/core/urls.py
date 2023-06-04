from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'),
    path('edicao/<str:id>/', views.edicao, name='edicao'),
    path('atualizacao/', views.atualizacao, name='atualizacao'),
    path('operacional/', views.operacional, name='operacional'),

]
