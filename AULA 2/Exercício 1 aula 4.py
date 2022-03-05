preco = float(input('Preço do produto: '))
qtd = int(input('Quantidade: '))
total = preco * qtd
if total >= 200.00:
    opcao = input('Desconto [D] ou parcelamento [P]: ')
    if opcao=='D':
        desc = 0.05*total
        total -= desc
        print('Desconto de R$ %.2f' % desc)
    else:
        p = int(input('Quantidade de parcelas: '))
        print('%d parcelas de R$ %.2f' % (p, total/p))

print('Total: R$ %.2f' % total)
