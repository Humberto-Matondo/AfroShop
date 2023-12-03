from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from utils.validacpf import valida_cpf
import re
# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= 'usuário')
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default= 'SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )

    )
    
    def __str__(self):
        return f'{self.usuario}'
    
    def clean(self):
        error_massages = {}

        if not valida_cpf(self.cpf):
            error_massages['cpf'] = 'CPF esta errado.'
        
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_massages['cep'] = 'Digite um CEP Valido, apenas 8 numeros.'
        
        if error_massages:
            raise ValidationError(error_massages)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'