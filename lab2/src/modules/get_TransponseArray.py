import numpy

# Функция принимает параметры
# arr - двумерная матрица

# Возвращает транспонированную матрицу

# Например, дана матрица
#[[1 2 3]
# [4 5 6]]
# Функция возвратит
#[[1 4]
# [2 5]
# [3 6]]
def get_TransponseArray(arr):
    result = numpy.zeros( (len(arr[0]), len(arr)), dtype = numpy.int )
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            result[j][i] = arr[i][j]
    return result
