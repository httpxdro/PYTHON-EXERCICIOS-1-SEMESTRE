a = float(input('Lado a = '))
b = float(input('Lado b = '))
c = float(input('Lado c = '))

if a < b + c and b < a + c and c < a + b:
    print('Formam')
else:
    print('Não formam')
    
