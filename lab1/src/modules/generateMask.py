# Принимает параметр U, например, [1,2,3,4,5,6,7,8,9,10,11]
# Принимает параметр A, например, [1,3,4,7]
# Возвращает сгенерированную маску A: [1,0,1,1,0,0,1,0,0,0,0]
def generateMask(U, A):
    maskA = []

    for i in range(len(U)):
        maskA.append(0)

    for i in range(len(U)):
        for j in range(len(A)):
            if U[i] == A[j]:
                maskA[i] = 1

    return maskA
