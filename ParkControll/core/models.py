from djongo import models

class UsuarioModel(models.Model):
    nome = models.CharField('login',max_length=30)
    email = models.CharField('email',max_length=150)
    senha = models.CharField('senha',max_length=25)
    permissao = models.IntegerField('permissao')
   
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Usuarios'    

class VeiculoModel(models.Model):
    placa = models.CharField('placa',max_length=11)
    tipo = models.CharField('tipo', max_length=30)
    marca = models.CharField('marca', max_length=30)
    modelo = models.CharField('modelo', max_length=30)
    cor = models.CharField('cor',max_length=30)
    proprietario = models.CharField('proprietario', max_length=150)
    cpf_proprietario = models.CharField('cpf_proprietario', max_length=11)
    telefone = models.CharField('telefone', max_length=11)
    status = models.CharField('status', max_length=20, default='Não Estacionado')

    def __str__(self):
        return self.placa
    
    class Meta:
        verbose_name_plural = 'Veiculos'

class OperacionalModel(models.Model):
    placa = models.CharField('placa',max_length=11)
    entrada = models.DateTimeField()
    saida = models.DateTimeField()

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name_plural = 'Operacional'