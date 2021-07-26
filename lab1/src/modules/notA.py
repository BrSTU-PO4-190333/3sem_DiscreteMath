from modules.generateMask import generateMask
from modules.getArrayFromMask import getArrayFromMask

# Принимает параметр U, например, [1,2,3,4,5,6,7,8,9,10,11]
# Принимает параметр A, например, [1,3,4,7]
# Возвращает готовый массив not A = [2,5,6,8,9,10,11]
def notA(U, A):
    maskA = generateMask(U, A)

    for i in range(len(U)):
        if maskA[i] == 1:
            maskA[i] = 0
        else:
            maskA[i] = 1

    return getArrayFromMask(U, maskA)
