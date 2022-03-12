n = int(input('n: '))
d = 2
while d < n:
    if n%d == 0:
        break
    d += 1
if d==n:
    print('Primo')
else:
    print('Não primo')
