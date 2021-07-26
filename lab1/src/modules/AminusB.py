from modules.generateMask import generateMask
from modules.getArrayFromMask import getArrayFromMask

# Принимает параметр U, например, [1,2,3,4,5,6,7,8,9,10,11]
# Принимает параметр A, например, [1,3,4,7]
# Принимает параметр B, например, [3,5,6,7,8]
# Возвращает готовый массив A \ B = [5,6,8]
def AminusB(U, A, B):
    maskA = generateMask(U, A)
    maskB = generateMask(U, B)

    mask = []
    for i in range(len(U)):
        if maskA[i] & ( not maskB[i]):
            mask.append(1)
        else:
            mask.append(0)

    return getArrayFromMask(U, mask)