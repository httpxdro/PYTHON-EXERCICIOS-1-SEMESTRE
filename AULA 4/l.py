n = int(input('n? '))
m = int(input('valor? '))
for i in range(n-1):
    x = int(input('valor? '))
    if x < m:
        m = x
print(m)
