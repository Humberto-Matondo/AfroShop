from django.contrib import admin
from .forms import VariacaoObrigatoria
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 0
    formset = VariacaoObrigatoria
    min_num = 1
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','descrisao_curta','get_preco_formatado', 
                    'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]

# Register your models here.
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
