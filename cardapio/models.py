from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cardapio(models.Model):
    '''Representa um cardapio'''
    data_cardapio = models.DateField()
    prato_principal = models.CharField(max_length=200, null=False)
    sobremesa = models.CharField(max_length=200)
    info_nutricionais = models.TextField(max_length=500)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, related_name="usuario")

    def __str__(self):
        return self.data_cardapio


    @property
    def get_usuario(self):
        return self.usuario.username