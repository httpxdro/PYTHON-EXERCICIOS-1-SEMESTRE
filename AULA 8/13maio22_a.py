def exibe(v, n, rotulo):
    print('%s:' rotulo, end=' ')
    for i in range(n):
        print(v[i], end=' ')
    print()
    
def intercala_vetores (a, b, c, tam1, tam2):
    i = 0
    j = 0
    k = 0
    while i<tam1 and j<tam2:
        if a [i] < b[j]:
            c [k] = a[i]
            i += 1
        elif b[j] < a[i]:
            c[k] = b[j]
            j += 1
        else:
            c[k] = a[i]
            i += 1
            j += 1
        k +=1
        while i<tam1:
            c[k] = a[i]
            i += 1
            k +=1
        while j<tam2:
            c[k] = b[j]
            j += 1
            k +=1
        return k

    a = [10, 15, 70, 80]
    b = [5, 20, 30, 70, 200]
    c = 9*[0]
    tam3 = intercala_vetores(a, b, c, 4, 5)
    exibe(a, 4, 'a')
    exibe(b, 5, 'b')
    exibe(c, tam3, 'c')
