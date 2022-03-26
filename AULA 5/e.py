n = int(input('x? '))

for x in range(n):
    fat = 1

    for i in range(1, x+1):
        fat = fat * i

    print('%d! = %d' % (x, fat))

