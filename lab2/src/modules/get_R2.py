import numpy

# Функция принимает параметры
# A - множество, например, A = [1,2,3,4,5,6,7,8,9,10]

# Возвращает отношение a = 2b в виде массива нулей и едениц

# Пусть множество A = [1,2,3,4,5,6]
# Тогда функция возвратит [(2, 1), (4, 2), (6, 3)]
#[[0 0 0 0 0 0]
# [1 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 1 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 1 0 0 0]]
def get_R2(A):
    R2 = numpy.zeros( (len(A), len(A)), dtype = numpy.int )
    for i in range(len(R2)):
        for j in range(len(R2[i])):
            a = A[i]
            b = A[j]
            if a == 2 * b:
                R2[i][j] = 1
    return R2