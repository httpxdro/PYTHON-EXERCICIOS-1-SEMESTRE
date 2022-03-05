n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
if n1 < n2:
    print('0 menor número é: ', n1)
    print('O maior número é: ', n2)

elif n1 == n2:
    print('Ambos são iguais')
else:
    print('O menor número é: ', n2)
    print('O maior número é: ', n1)
print('A soma dos números é: ', n1+n2)
