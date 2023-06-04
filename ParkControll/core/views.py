from django.shortcuts import render, HttpResponse
from .models import UsuarioModel, VeiculoModel, OperacionalModel
from .forms import UsuarioModelForm, VeiculoModelForm, OperacionalModelForm

def index(request):
    return render(request, 'index.html')

def consulta(request):

    veiculos = []
    veiculos = VeiculoModel.objects.all()
    context = {'listaVeiculos': veiculos}

    if request.method == 'POST':       
        pesquisa = request.POST.get('pesquisa')

        if request.POST.get('busca') == 'placa':
            
            return HttpResponse('buscando pela placa: ' + pesquisa)
        else:
            return HttpResponse('buscando pelo proprietario: ' + pesquisa)
    else:        
        return render(request, 'consulta.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = VeiculoModelForm(request.POST)        
        veiculo = VeiculoModel()
        veiculo.placa = form.data['placa']
        veiculo.tipo = form.data['tipo']
        veiculo.marca = form.data['marca']
        veiculo.modelo = form.data['modelo']
        veiculo.cor = form.data['cor']
        veiculo.proprietario = form.data['proprietario']
        veiculo.cpf_proprietario = form.data['cpf']
        veiculo.telefone = form.data['telefone']
        veiculo.save()    
    return render(request, 'cadastro.html')

def edicao(request):
    return render(request, 'edicao.html')

def operacional(request):
    return render(request, 'operacional.html')