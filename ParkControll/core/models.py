from djongo import models


class UsuarioModel(models.Model):
    nome = models.CharField('nome',max_length=150)
    email = models.CharField('email',max_length=150)
    senha = models.CharField('senha',max_length=150)
    permissao = models.IntegerField('permissao')


    def __str__(self):
        return self.nome


class VeiculoModel(models.Model):
    placa = models.CharField('placa',max_length=11)
    tipo = models.CharField('tipo', max_length=30)
    marca = models.CharField('marca', max_length=30)
    modelo = models.CharField('modelo', max_length=30)
    cor = models.CharField('cor',max_length=30)
    proprietario = models.CharField('proprietario', max_length=150)
    cpf_proprietario = models.IntegerField('cpf_proprietario')
    telefone = models.IntegerField('telefone')

    def __str__(self):
        return self.placa

class OperacionalModel(models.Model):
    placa = models.CharField('placa',max_length=11)
    entrada = models.DateTimeField(
        verbose_name='Entrada veículo',
        auto_now_add=False, 
        auto_now=True
    )
    saida = models.DateTimeField(
        verbose_name='Saída veículo',
        auto_now_add=False, 
        auto_now=True
    )

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name_plural = 'Veículos'