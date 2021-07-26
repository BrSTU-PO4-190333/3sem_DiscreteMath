# Функция принимает параметры:
# arr - массив из нулей и единиц

# Возвращает матрицу после алгоритма Флоида Уоршала
def FloydWarshallAlgorithm(arr):
    R = arr.copy()
    for k in range(len(R)):
        for i in range(len(R)):
            for j in range(len(R)):
                R[i][j] = R[i][j] or R[i][k] and R[k][j]
    return R