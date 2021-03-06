# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_cardapio_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='data_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da ultima atualização'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='data_cardapio',
            field=models.DateField(verbose_name='Data do prato'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='info_nutricionais',
            field=models.TextField(verbose_name='Informações Nutricionais'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='prato_principal',
            field=models.CharField(max_length=200, verbose_name='Prato Principal'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='sobremesa',
            field=models.CharField(max_length=200, verbose_name='Sobremesa'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
