a = float(input('Lado a = '))
b = float(input('Lado b = '))
c = float(input('Lado c = '))

if a < b + c and b < a + c and c < a + b:
    print('Formam')
    if a == b and b == c:
        print('Equilátero')
    elif a == b or a == c or b==c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não formam')
    


