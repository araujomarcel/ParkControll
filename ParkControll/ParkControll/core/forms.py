from .models import UsuarioModel, VeiculoModel, OperacionalModel
from django.forms import ModelForm

class UsuarioModelForm(ModelForm):
    class Meta:
        model = UsuarioModel
        fields = ['nome', 'email', 'senha', 'permissao']

class VeiculoModelForm(ModelForm):
    class Meta:
        model = VeiculoModel
        fields = ['placa','tipo','marca','modelo','cor','proprietario','cpf_proprietario','telefone', 'status']

class OperacionalModelForm(ModelForm):
    class Meta:
        model = OperacionalModel
        fields = ['placa', 'entrada', 'saida']
