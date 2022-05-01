def maximo(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input('Numero: '))
y = int(input('Numero: '))

m = maximo(x, y)

print('Maximo: %d' % m)
