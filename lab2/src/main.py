from modules.get_R1 import get_R1 # Task 1-1
from modules.get_R2 import get_R2 # Task 1-1
from modules.print_R import print_R # Task 1-1
from modules.print_couple import print_couple # Task 1-1
from modules.get_TransponseArray import get_TransponseArray # Task 1-2
from modules.get_addiction import get_addiction # Task 1-2
from modules.FloydWarshallAlgorithm import FloydWarshallAlgorithm # Task 1-4
from modules.print_composition import print_composition # Task 1-5
from modules.print_type_func import print_type_func # Task 3

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]

    R1 = get_R1(A)
    print('Отношение R1')
    print_R(A, R1)
    print_couple(A, R1)

    R1T = get_TransponseArray(R1)
    print('Обратное отношение R1^-1')
    print_R(A, R1T)
    print_couple(A, R1T)

    R1addiction = get_addiction(R1)
    print('Дополнение R1 =')
    print_R(A, R1addiction)
    print_couple(A, R1addiction)

    R2 = get_R2(A)
    print('Отношение R2')
    print_R(A, R2)
    print_couple(A, R2)

    R2T = get_TransponseArray(R2)
    print('Обратное отношение R2^-1')
    print_R(A, R2T)
    print_couple(A, R2T)

    R2_addiction = get_addiction(R2)
    print('Дополнение R2')
    print_R(A, R2_addiction)
    print_couple(A, R2_addiction)

    print('Композиция R1oR2')
    print_composition(A, R1, R2)

    print('Композиция R2oR1')
    print_composition(A, R2, R1)

    FWA_R1 = FloydWarshallAlgorithm(R1)
    print('Отношение R1 после алгоритма Флоида-Уоршала')
    print_R(A, FWA_R1)
    print_couple(A, FWA_R1)

    FWA_R2 = FloydWarshallAlgorithm(R2)
    print('Отношение R2 после алгоритма Флоида-Уоршала')
    print_R(A, FWA_R2)
    print_couple(A, FWA_R2)

    B = [1,2,3,4]
    C = [5,6,7,8]
    print('Определение функция это или нет и нахождение его свойств')

    print('Variant 1')
    print_type_func( B, C, [(1,5), (2,5), (3,6), (4,8)] ) 

    print('Variant 2')
    print_type_func( B, C, [(1,5), (2,8), (4,6), (4,7)] ) 

    print('Variant 3')
    print_type_func( B, C, [(1,5), (2,5), (3,6), (3,7), (4,8)] ) 

    print('Variant 4')
    print_type_func( B, C, [(1,8), (2,6), (3,5), (4,7)] ) 

    print('Variant 5')
    print_type_func( B, C, [(1,5), (2,5), (3,5), (4,7)] ) 

    print('Variant 6')
    print_type_func( B, C, [(1,7), (2,6), (4,5)] ) 

    print('Variant 7')
    print_type_func( B, C, [(1,8), (2,6), (3,8), (4,6)] )

    print('Variant 8')
    print_type_func( B, C, [(1,5), (2,5), (3,6), (4,8)] )

    print('Variant 9')
    print_type_func( B, C, [(1,5), (2,7), (3,6), (4,8)] )

    print('Variant 10')
    print_type_func( B, C, [(1,8), (2,7), (3,5), (4,6)] )

    print('Variant 11')
    print_type_func( B, C, [(1,5), (2,5), (3,6), (4,8), (3,8)] )

    print('Variant 12')
    print_type_func( B, C, [(1,5), (2,5), (3,6), (4,8)] )

    print('Variant 14 (13)')
    print_type_func( B, C, [(1,6), (2,8), (3,5), (4,7)] )

    print('Variant 15 (14)')
    print_type_func( B, C, [(1,5), (2,6), (3,7), (4,6)] )

    print('Test 1')
    print_type_func(B, C, [(1,5), (2,5), (3,6), (4,7)])

    print('Test 2')
    print_type_func(B, C, [(1,6), (2,5), (3,7), (4,8)])

    print('Test 3')
    print_type_func(B, C, [(1,5), (2,6), (3,6), (1,7)])
