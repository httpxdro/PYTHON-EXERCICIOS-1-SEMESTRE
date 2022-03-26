while True:
    credito = float(input('Créditos: '))
    carrinho = 0.0
    item = float(input('Item: '))
    while item != 0.0:
        if carrinho+item > credito:
            print('Crédito insuficiente')
        else:
            carrinho += item
        item = float(input('Item: '))
    print('Carrinho: R$ %.2f' % carrinho)
    clientes = input('\nHá mais clientes? ')
    if clientes == 'N': break
