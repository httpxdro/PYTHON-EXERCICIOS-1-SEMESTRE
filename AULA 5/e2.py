n = int(input('x? '))

for x in range(n):
    termial = 0

    for i in range(1, x+1):
        termial = termial + i

    print('%d? = %d' % (x, termial))

