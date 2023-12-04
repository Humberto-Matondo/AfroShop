from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

# Create your views here.

class ListaProdutos(ListView):
    pass

class DetalheProduto(View):
    pass

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass
