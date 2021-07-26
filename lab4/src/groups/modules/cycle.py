def cycle(A, mod):
    for i in range(len(A)):
        mySet = set()
        e = 1
        print('<%d> = {' % (A[i]))
        for j in range(len(A)):
            print('\t(%d * <%d>) mod %d = ' % (e, A[i], mod), end = '')
            e = (e * A[i]) % mod
            print('%d,' % (e))
            mySet.add(e)
        print('} = ', mySet, ' - порядок %d' % (len(mySet)))
