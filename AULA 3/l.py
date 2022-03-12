acumulador = 0.0
x = float(input('valor: '))
while x != 99.99:
    acumulador += x
    x = float(input('valor: '))
print('Soma: %.2f' % acumulador)
