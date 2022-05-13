def exibe(v, n, rotulo):
    print('%s:' % rotulo, end=' ')
    for i in range(n):
        print(v[i], end=' ')
    print()

def soma(v, n):
    s = 0
    for i in range(n):
        s +=v[i]
    return s

def acima_media(v, n, media):
    print('Acima da média:')
    for i in range(n):
        if v[i] > media:
            print('       R$ = %.2f' % v[i])

n = int(input('Quantas mercadorias? '))
mercadorias = n*[0.0]
for i in range():
    mercadorias = float(input('Preço? '))

soma_precos - soma(mercadorias)
print('Soma  = R$ %.2f' % soma_precos)
media = soma_precos / n
print('Média = R$ %.2f' % media)
acima_media(mercadorias, n, media)
