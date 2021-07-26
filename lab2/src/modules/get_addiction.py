import numpy

# Функция принимает параметры
# arr - массив из нулей и единиц

# Возвращает дополнение отношения
# (Меняет в матрице нули на еденицы)

# Например, дан массив
# [[0,0,0]
#  [0,1,0]]
# Функция возвратит
# [[1,1,1] 
#  [1,0,1]]
def get_addiction(arr):
    result = numpy.zeros( (len(arr), len(arr[0])), dtype = numpy.int)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            result[i][j] = 0 if (arr[i][j] == 1) else 1
    return result
