from modules.getKeliTable import getKeliTable_a_times_b_mod
from modules.printNetralElement import printNetralElement_a_times_b_mod
from modules.printReverseElement import printReverseElement
from modules.cycle import cycle
from modules.printH import printH
from modules.printHKeliTable import printHKeliTable

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    mod = 13

    arr = getKeliTable_a_times_b_mod(A, mod)

    e = printNetralElement_a_times_b_mod(arr)

    printReverseElement(A, arr, e)

    cycle(A, mod)

    k = [1, 12]
    arr2 = getKeliTable_a_times_b_mod(k, mod)

    k = [1, 3, 9]
    arr2 = getKeliTable_a_times_b_mod(k, mod)

    k = [1, 5, 8, 12]
    arr2 = getKeliTable_a_times_b_mod(k, mod)

    k = [1, 3, 4, 9, 10, 12]
    arr2 = getKeliTable_a_times_b_mod(k, mod)

    ArrH = printH(A, mod, [1, 12])
    printHKeliTable(A, mod, ArrH)