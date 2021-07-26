# Принимает параметр U, например, [1,2,3,4,5,6,7,8,9,10,11]
# Принимает параметр maskA, например, [1,0,1,1,0,0,1,0,0,0,0]
# Возвращает готовый массив [1,3,4,7]
def getArrayFromMask(U, maskA):
    returnArr = []

    for i in range(len(U)):
        if maskA[i] == 1:
            returnArr.append(U[i])

    return returnArr