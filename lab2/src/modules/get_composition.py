import numpy
from modules.get_couple import get_couple

# Функция принимает параметры
# A - множество, например, A = [1,2,3,4,5,6,7,8,9,10]
# R1 - матрица отношения, состоящая из нулей и единиц
# R2 - матрица отношения, состоящая из нулей и единиц

# Из R1 сосдает пары
# Из R2 сосдает пары
# Возвращает композицию R1 и R2
# (Если R1[1] = R2[0], то получает картедж (R1[0], R2[1]))

# Например,
# R1 = [ (3,1), (6,2) ]
# R2 = [ (1,3), (2,2), (3,1) ]
# Функция возвратит
# [ (3,3), (6,2) ]

# Например,
# R1 = [ (1,3), (2,2), (3,1) ]
# R2 = [ (3,1), (6,2) ]
# Функция возвратит
# [ (1,1) ]
def get_composition(A, R1, R2):
    coupleR1 = get_couple(A, R1)
    coupleR2 = get_couple(A, R2)

    coupleR1oR2 = []
    for i in range(len(coupleR1)):
        for j in range(len(coupleR2)):
            if coupleR1[i][0] == coupleR2[j][1]:
                coupleR1oR2.append( (coupleR2[j][0], coupleR1[i][1]) )

    arr = numpy.zeros( (len(A), len(A)), dtype = int )
    for k in range(len(coupleR1oR2)):
        i = A.index(coupleR1oR2[k][0])
        j = A.index(coupleR1oR2[k][1])
        arr[i][j] = 1

    return arr
