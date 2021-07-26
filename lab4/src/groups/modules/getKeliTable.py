import numpy

# Функция принимает параметры:
# A - Множество, например, A = {1,2,3,4,5,6,7,8,9,10,11,12}
# mod - по какому моду брать
# Функция возвращает массив (таблицу Кэли) с готовой группой a*b mod n
def getKeliTable_a_times_b_mod(A, mod):
    returnArray = numpy.zeros( (len(A), len(A)), dtype=int )
    for i in range(len(A)):
        for j in range(len(A)):
            returnArray[i][j] = (A[i] * A[j]) % mod

    print('Таблица Кэли для %a' % A)
    print(returnArray)    
    
    return returnArray
