from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cardapio(models.Model):
    '''Representa um cardapio'''
    data_cardapio = models.DateField('Data do prato')
    prato_principal = models.CharField('Prato Principal', max_length=200, null=False)
    sobremesa = models.CharField('Sobremesa',max_length=200)
    info_nutricionais = models.TextField('Informações Nutricionais')
    data_cadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    data_update = models.DateTimeField('Data da ultima atualização', auto_now=True)
    usuario = models.ForeignKey(User, related_name="usuario")

    def __str__(self):
        return self.data_cardapio


    @property
    def get_usuario(self):
        return self.usuario.username