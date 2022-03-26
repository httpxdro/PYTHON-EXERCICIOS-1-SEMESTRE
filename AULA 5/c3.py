x = input('Caractere: ')
L = int(input('Linhas: '))

for i in range(L):
    for j in range(i+1):
        print(x, end='')
    print()
for i in range(L):
    for j in range(L-i):
        print(x, end='')
    print()
