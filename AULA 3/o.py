e = input('Calcular? ')
while e=='s':

a = int(input('a: '))
b = int(input('b: '))
op = input('operador: ')
if op=='+': r = a+b
elif op=='-': r = a-b
elif op=='*': r = a*b
elif op=='/':
if b==0:
print('Divisão por zero!')
break
else:
r = a/b

print('%d %c %d = %d\n' % (a,op,b,r))
e = input('Calcular? ')
