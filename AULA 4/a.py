n = int(input('n: '))
while True:
    print(n % 10, end='')
    n = n // 10
    if n==0: break
