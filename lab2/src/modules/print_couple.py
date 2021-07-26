# Функция принимает параметры
# A - множество, например, A = [1,2,3,4,5,6,7,8,9,10]
# arr - матрица отношения, состоящая из нулей и единиц

# Печатает пары отношения

# Например, множество A = [3, 5, 7]
# arr = [
#   [1,0,1]
#   [0,1,0]
#   [0,1,1]
# ]
# Функция напечатает отношение
# {       (3, 3), (3, 7), (5, 5), (7, 5), (7, 7) }
def print_couple(A, arr):
    data = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                data.append( (A[i], A[j]) )
    if data != []:
        print('{\t', end = '')
        k = 0
        for i in range(len(data) - 1):
            k += 1
            if k == 7:
                k = 1
                print(end = '\n\t')
            print(data[i], end = ', ')
        print(data[len(data) - 1], end = '')
        print(' }')
    else:
        print('{  }')
    return data
