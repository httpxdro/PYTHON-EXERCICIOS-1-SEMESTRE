p = int(input('p? '))
u = int(input('u? '))


for x in range(p, u+1):
    qtd = 0

    for divisor in range(1, x+1):
        if x % divisor == 0:
            qtd += 1

    if qtd == 2:
        print(x, end=' ')
