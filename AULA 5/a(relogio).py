from time import sleep

while True:
    h = 0
    while h < 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print('%02d:%02d:%02d' % (h,m,s))
                s += 1
                sleep(1)
            m += 1
        h += 1
