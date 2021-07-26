import numpy

# Функция принимает параметры
# B - множество иксов, например, B = [ 1,2,3,4 ]
# C - множество игреков, например, C = [ 5,6,7,8 ]
# S - отношение в виде матрицы из нулей и единиц S = [ (1,6), (2,5), (3,7), (4,8) ]

# Функция печатает характеристики
# Определеяет это функция или не функция
# Определяет функция сурьективна или несурьективна
# Определяет функция инъективна или неинъективна
# Определяет функция биективна или небиективна
def print_type_func(B, C, S):
    isFunc = 1
    isSurjection = 1
    isInjectivity = 1
    isBijection = 1

    arr = numpy.zeros( (len(B), len(C)), dtype = numpy.int )
    for i in range(len(B)):
        for j in range(len(C)):
            for k in range(len(S)):
                if B[i] == S[k][0] and C[j] == S[k][1]:
                    arr[i][j] = 1
    print(arr)

    # Функция
    for i in range(len(B)):
        sum = 0
        for j in range(len(C)):
            if arr[i][j] == 1:
                sum += 1
        if sum != 1:
            isFunc = 0
            break
    if isFunc == 1:
        # Сурьекция
        for j in range(len(C)):
            sum = 0
            for i in range(len(B)):
                if arr[i][j] == 1:
                    sum += 1
            if sum == 0:
                isSurjection = 0
        
        # Инъекция
        for j in range(len(C)):
            sum = 0
            for i in range(len(B)):
                if arr[i][j] == 1:
                    sum += 1
            if sum > 1:
                isInjectivity = 0
                break

        # Биекция
        for i in range(len(B)):
            sum = 0
            for j in range(len(C)):
                if arr[i][j] == 1:
                    sum += 1
            if sum != 1:
                isBijection = 0
                break
        if isBijection == 1:
            for j in range(len(C)):
                sum = 0
                for i in range(len(B)):
                    if arr[i][j] == 1:
                        sum += 1
                if sum != 1:
                    isBijection = 0
                    break

    if isFunc != 1:
        print('Это не функция => исследования не проводим')
    else:
        print('Это функция => проводим исследования')

        print('%16s | ' % 'Сурьекция', end = '')
        if isSurjection == 1:
            print('+')
        else:
            print('-')

        print('%16s | ' % 'Инъекция', end = '')
        if isInjectivity == 1:
            print('+')
        else:
            print('-')

        print('%16s | ' % 'Биекция', end = '')    
        if isBijection == 1:
            print('+')
        else:
            print('-') 

        print('%16s | ' % 'Биекция', end = '')
        if isSurjection == 1 and isInjectivity == 1:
            print('+')
        else:
            print('-')

    print()
