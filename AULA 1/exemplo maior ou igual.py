prod = float(input('Preço do produto: '))
qtd = int(input('Quantidade: '))
total = prod * qtd
if total >= 150.00:
    total = 0.85 * total
print('Total a pagar: R$ %.2f' % total)
