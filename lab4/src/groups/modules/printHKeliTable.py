import numpy

def printHKeliTable(A, mod, arr):
    # шапка таблицы
    print('%4s |' % '', end = '')
    for a in range(len(A) + 1):
        if a == 0:
            print('%4sH' % '', end='')
        else:
            print('%4dH' % (a), end='')
    print()
    # полоса под шапкой таблицы
    for a in range(len(A) + 1 + 1):
        print('-----', end = '')
    print()
    # тело таблицы
    for a in range(len(A) + 1):
        if a == 0:
            print('%4sH|' % '', end='')
        else:
            print('%4dH|' % (a), end='')
        for b in range(len(A) + 1):
            index = (arr[a][0] + arr[b][len(arr[a])-1]) % mod
            if index == 0:
                print('%4sH' % '', end='')
            else:
                print('%4dH' % (index), end='')
        print()
