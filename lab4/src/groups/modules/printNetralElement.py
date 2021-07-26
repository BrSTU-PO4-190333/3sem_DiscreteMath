# Функция принимает параметры
# arr - массив, которой лежит результат группы a*b mod n
# Функция печатает нейтральные элементы
# Если arr[i][j] * arr[j][i] == arr[i][j], то это нейтральный элемент
# a * e = e * a = a
def printNetralElement_a_times_b_mod(arr):
    print()
    print('a * e = e * a = a')
    print('e - нейтральный элемент')
    e = -1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Если a * e = a
            if (arr[i][j] * arr[j][i]) == arr[i][j]:
                print('arr[%2d][%2d] = e = %d' % (i, j, arr[j, i]))
                e = arr[j][i]
    print()
    return e