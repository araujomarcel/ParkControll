from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def consulta(request):
    return render(request, 'consulta.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def edicao(request):
    return render(request, 'edicao.html')

def operacional(request):
    return render(request, 'operacional.html')