# Функция принимает параметры
# A - множество, например, A = [1,2,3,4,5,6,7,8,9,10]
# R - отношение в виде матрицы из нулей и единиц

# Печатает матрицу с столбцами и строками с элементами из множества A
def print_R(A, R):

    print('%4s|' % '', end = '')
    for i in range(len(A)):
        print('%4d' % A[i], end = '')
    print('|')

    print('%4s|' % '----', end = '')
    for i in range(len(A)):
        print('%4s' % '----', end = '')
    print('|')

    for i in range(len(R)):
        print('%4d|' % A[i], end = '')
        for j in range(len(R[i])):
            print('%4d' % R[i][j], end = '')
        print('|')

    print('%4s|' % '----', end = '')
    for i in range(len(A)):
        print('%4s' % ' ---', end = '')
    print('|')
    print()
