import copy

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.list import ListView

from . import forms, models

# Create your views here.

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho', {}))
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                    usuario=self.request.user
                ).first()

            self.contexto = {
                'userform': forms.UserForm(data = self.request.POST or None, usuario=self.request.user, instance= self.request.user),
                'perfilform': forms.PerfilForm(data = self.request.POST or None, instance= self.perfil),
            }
        else:
              self.contexto = {
                'userform': forms.UserForm(data = self.request.POST or None),
                'perfilform': forms.PerfilForm(data = self.request.POST or None),
            }   
        
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        if self.request.user.is_authenticated:
            self.template_name = 'perfil/atualizar.html'

        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
   def post(self, *args, **kwargs):
#        if not self.userform.is_valid() or not self.perfilform.is_valid():
        if not self.userform.is_valid():
            return self.renderizar

        usermame = self.userform.cleaned_data.get('usermame')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        if self.request.user.is_authenticated:
            usuario =  get_object_or_404(User, usermame= request.user.username)
            
            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            
            else:
                self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        else:

            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password: 
            autentica = authenticate(self.request, username=usuario, password=password)
            
            if autentica:
                login(self.request, user=usuario)

        self.request.ession['carrinho'] = self.carrinho
        self.request.session.save()
        return self.renderizar

class Atualizar(View):
    def get(self, *args, **kwargs):
        return 
class Login(View):
    def get(self, *args, **kwargs):
        return 

class Logout(View):
    def get(self, *args, **kwargs):
        return 
