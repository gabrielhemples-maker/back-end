preco = float(input(' qual é o preço de produto?R$'))
desconto = preco - (preco * 5 / 100)
print(' o pruduto que custava{:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))
