n1 = int(input('n1: '))
n2 = int(input('n2: '))
if n1==n2:
    print('Números iguais, ', end=' ')
    if n1%2==0:
        print('ambos pares.')
    else:
        print('ambos ímpares.')
else:
    print('Números diferentes.')
    
