from time import sleep

while True:
    h = 23
    while h >= 0:
        m = 59
        while m >= 0:
            s = 59
            while s >= 0:
                print('%02d:%02d:%02d' % (h,m,s))
                s -= 1
                sleep(1)
            m -= 1
        h -= 1
