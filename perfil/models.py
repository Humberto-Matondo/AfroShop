import re

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError


# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='Usuário')
    #cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
   
    def __str__(self):
        return f'{self.usuario}'
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis' 