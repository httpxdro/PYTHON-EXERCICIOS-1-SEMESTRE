x = float(input('x: '))
y = float(input('y: '))
if x < y:
    print('%.2f é menor que %.2f' % (x, y))
else:
    if x > y:
        print('%.2f é maior que %.2f' % (x, y))
    else:
        print('%.2f é igual a %.2f' % (x, y))
