from django.contrib import admin
from .models import  VeiculoModel, OperacionalModel

class VeiculoModelAdmin(admin.ModelAdmin):
    list_display = ('placa','tipo','marca','modelo','cor','proprietario','cpf_proprietario','telefone','status')

class OperacionalModelAdmin(admin.ModelAdmin):
    list_display = ('placa', 'entrada', 'saida')

admin.site.register(VeiculoModel, VeiculoModelAdmin)
admin.site.register(OperacionalModel, OperacionalModelAdmin)

