# Функция принимает параметры
# A - множество
# arr - массив
# e - нейтральный элемент
# Функция возвращает обратный элемент
# a * a^-1 = a^-1 * a = e
# Если в элементе массива arr нейтральный элемент e,
# то смотрим его индексы i, j
# - и определяем элементы a = A[i], a^-1 = A[j] 
def printReverseElement(A, arr, e):
    print()
    print('a * a^-1 = a^-1 * a = e')
    print('a^-1 - обратный элемент')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
                if arr[i][j] == e:
                    print('a = %-4d  ~  a^-1 = %-4d' % (A[i], A[j]))
