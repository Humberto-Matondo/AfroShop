from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from . import forms, models

# Create your views here.

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(data = self.request.POST or None, usuario=self.request.user, instance= self.request.user),
                'perfilform': forms.PerfilForm(data = self.request.POST or None),
            }
        else:
              self.contexto = {
                'userform': forms.UserForm(data = self.request.POST or None),
                'perfilform': forms.PerfilForm(data = self.request.POST or None),
            }   
            
        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar
class Criar(BasePerfil):
   def post(self, *args, **kwargs):
        return renderizar
class Atualizar(View):
    def get(self, *args, **kwargs):
        return 
class Login(View):
    def get(self, *args, **kwargs):
        return 

class Logout(View):
    def get(self, *args, **kwargs):
        return 
