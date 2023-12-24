from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.list import ListView

from produto.models import Variacao
from utils import utils

from .models import ItemPedido, Pedido

# Create your views here.

class Pagar(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Precisa fazer o login.'
                )
            return redirect('perfil:criar')
            
        if not self.request.session.get('carrinho'):
            messages.error(
                self.request,
                'O Carrinho esta Vazio.'
                )
            return redirect('produto:lista')
        
        
        carrinho = self.request.session.get('carrinho')    
        carrinho_variacao_ids = [v for v in carrinho]
        bd_variacao = list(
            variacao.objects.select_related('produto').filter(id__in=carrinho_variacao_ids)
        )

        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco_unt = carrinho[vid]['preco_unt']
            preco_unt_promo = carrinho[vid]['preco_unt_promo']
            
            error_msg_estoque = ''

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unt
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * preco_unt_promo

                error_msg_estoque = 'Estoques insuficiente! Reduzimos a quantidade desses produtos. Verifique os produtos afetados.'
            
            if error_msg_estoque:
                messages.error(
                    self.request,
                    error_msg_estoque,
                )
                self.request.session.save()
                return redirect('produto:carrinho')

        qtd_total_carrinho = utils.cart_total_quantidade_total_do_carrinho(carrinho)
        valor_total_carrinho = utils.cart_total(carrinho)

        pedido = Pedido(
            usuario = self.request.user, 
            total = valor_total_carrinho, 
            qtd_total= qtd_total_carrinho,
            status='C',
            )
        pedido.save()

        ItemPedido.objects.bulk_create(
           [
                ItemPedido(
                    pedido = pedido,
                    produto = v['produto_nome'],
                    produto_id = v['produto_id'],
                    variacao= v['variacao_nome'],
                    variacao_id = v['variacao_id'],
                    preco = v['preco_quantitativo'],
                    preco_promocional= v['preco_quantitativo_promocional'],
                    quantidade= v['quantidade'],
                    imagem= v['imagem'],
                ) for v in carrinho.values()
           ]
        )

        contexto = { }

        del self.request.session['carrinho']
        #return render(self.request, self.template_name, contexto)
        return redirect('pedido:lista')

class SalvarPedido(View):
    pass

class Detalhe(View):
    pass

class Lista(View):
    pass