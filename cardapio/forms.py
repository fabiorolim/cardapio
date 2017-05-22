from django.forms import models
from .models import Cardapio

class FormularioCardapio(models.ModelForm):
    class Meta:
        model = Cardapio
        exclude = ['data_cadastro', 'usuario']

