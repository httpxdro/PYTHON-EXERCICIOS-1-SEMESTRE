preco = float(input('Preço? '))
qtd = float(input('Quantidade? '))
porcentagem_desconto = float(input('Desconto? '))

total = preco * qtd

desconto = total * porcentagem_desconto / 100

final = total - desconto

print('Valor final = R$ %.2f' % final)

