a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))
d = float(input('d? '))
e = float(input('e? '))

m = a

if b>m:
    m = b
if c>m:
    m = c  
if d>m:
    m = d  
if e>m:
    m = e

print('maior =', m)

#poderiam ser escritos  if b>m: m = b  para melhor visualização
