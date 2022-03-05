preco = float(input('Preço? '))
qtd = float(input('Quantidade? '))

total = preco * qtd

desconto = total * 0.10

final = total - desconto

print('Valor final = R$ %.2f' % final)

