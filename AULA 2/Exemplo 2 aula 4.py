preco = float(input('Preço do produto: '))
qtd = int(input('Quantidade: '))
total = preco * qtd
if total > 200.00:
    opcao = input('Desconto [D] ou Parcelamento [P]: ')
    if opcao=='D':
        desc = 0.05*total
        total -= desc
        print('Desconto de R$ %.2f' % desc)
    else:
        print('4 parcelas de R$ %.2f' % (total/4))
print('Total: R$ %.2f' % total)
