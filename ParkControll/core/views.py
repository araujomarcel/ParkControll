from django.shortcuts import render, redirect, HttpResponse
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
            context['listaVeiculos'] = VeiculoModel.objects.filter(placa__icontains=pesquisa)            
            return render(request, 'consulta.html', context)
        else:
            context['listaVeiculos'] = VeiculoModel.objects.filter(proprietario__icontains=pesquisa)            
            return render(request, 'consulta.html', context)
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

def edicao(request, id):    
    veiculo = VeiculoModel.objects.get(placa=id)
    return render(request, 'edicao.html', {'form': veiculo})
   
def atualizacao(request):
    form = VeiculoModelForm(request.POST)  
    veiculo = VeiculoModel.objects.get(id=form.data['id'])

    veiculo.placa = form.data['placa']
    veiculo.tipo = form.data['tipo']
    veiculo.marca = form.data['marca']
    veiculo.modelo = form.data['modelo']
    veiculo.cor = form.data['cor']
    veiculo.proprietario = form.data['proprietario']
    veiculo.cpf_proprietario = form.data['cpf']
    veiculo.telefone = form.data['telefone']

    veiculo.save()    
    return redirect('consulta')

def edicao(request, id):    
    veiculo = VeiculoModel.objects.get(placa=id)
    return render(request, 'edicao.html', {'form': veiculo})

def exclusao(request, id):    
    veiculo = VeiculoModel.objects.get(placa=id)
    if veiculo != None:
        veiculo.delete()
    
    return consulta(request)

def operacional(request):
    return render(request, 'operacional.html')