from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [    
    path('', views.index, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'),
    path('edicao/<str:id>/', views.edicao, name='edicao'),
    path('exclusao/<str:id>/', views.exclusao, name='exclusao'),
    path('atualizacao/', views.atualizacao, name='atualizacao'),
    path('historico/<str:id>/', views.historico, name='historico'),
    path('operacional/', views.operacional, name='operacional'),
    path('entrada/<str:id>/', views.entrada, name='entrada'),
    path('saida/<str:id>/', views.saida, name='saida'),
]
