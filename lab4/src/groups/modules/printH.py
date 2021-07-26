import numpy

def printH(A, mod, H):
    arr = numpy.zeros( (len(A) + 1, len(H)), dtype=int )    
    for j in range(len(H)):
        arr[0][j] = H[j]

    print('    H =', arr[0])
    for i in range(len(A)):
        print('%4dH = ' % (i + 1), end='')
        for j in range(len(H)):
            arr[i+1][j] = ( H[j] + (i+1) ) % mod
        print(arr[i+1])

    return arr
