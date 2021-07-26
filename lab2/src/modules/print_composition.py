from modules.get_couple import get_couple
from modules.print_couple import print_couple
from modules.get_composition import get_composition

# Функция принимает параметры
# A - множество, например, A = [1,2,3,4,5,6,7,8,9,10]
# R1 - матрица отношения, состоящая из нулей и единиц
# R2 - матрица отношения, состоящая из нулей и единиц

# Перводит R1 в пары
# Перводит R2 в пары
# Получает матрицу композиции R1oR2
# Печатает композицию отношений R1 и R2
def print_composition(A, R1, R2):
    coupleR1 = get_couple(A, R1)
    coupleR2 = get_couple(A, R2)
    R1oR2 = get_composition(A, R1, R2)
    
    print()
    print_couple(A, R1)
    print('o')
    print_couple(A, R2)
    print('=')
    print_couple(A, R1oR2)
    print()
