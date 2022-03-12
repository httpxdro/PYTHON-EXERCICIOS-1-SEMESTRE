#m = maior

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))

m = a

if b>m:
    m = b
#else:
#    m = m  não fazer isso
if c>m:
    m = c
#else:
#    m = m  não fazer isso

print('maior =', m)
