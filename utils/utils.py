def formata_preco(val):
    return f'${val:.2f}'.replace('.', ',')

def cart_total_quantidade_total_do_carrinho(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])

def cart_total(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo') 
            for item 
            in carrinho.values()
        ]
    )