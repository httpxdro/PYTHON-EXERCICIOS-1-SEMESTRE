acumulador = 0
x = float(input('valor: '))
while x != 99.99:
    if x > 0:
        acumulador += x
    x = float(input('valor: '))
print('Soma positivos: %.2f' % acumulador)
