n = int(input('n? '))
i = 1

while i * i <= n:
    i += 1
    
i -= 1

print('Quadrado mais próximo: ', i*i)
