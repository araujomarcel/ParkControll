from .models import VeiculoModel, OperacionalModel
from django.forms import ModelForm

class VeiculoModelForm(ModelForm):
    class Meta:
        model = VeiculoModel
        fields = ['placa','tipo','marca','modelo','cor','proprietario','cpf_proprietario','telefone', 'status']

class OperacionalModelForm(ModelForm):
    class Meta:
        model = OperacionalModel
        fields = ['placa', 'entrada', 'saida']
