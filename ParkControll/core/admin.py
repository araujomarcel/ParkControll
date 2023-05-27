from django.contrib import admin
from .models import UsuarioModel, VeiculoModel, OperacionalModel

class UsuarioModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha', 'permissao')

class VeiculoModelAdmin(admin.ModelAdmin):
    list_display = ('placa','tipo','marca','modelo','cor','proprietario','cpf_proprietario','telefone')

class OperacionalModelAdmin(admin.ModelAdmin):
    list_display = ('placa', 'entrada', 'saida')

admin.site.register(UsuarioModel, UsuarioModelAdmin)
admin.site.register(VeiculoModel, VeiculoModelAdmin)
admin.site.register(OperacionalModel, OperacionalModelAdmin)

