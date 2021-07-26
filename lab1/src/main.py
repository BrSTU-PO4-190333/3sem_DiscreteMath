import random
import time
import matplotlib.pyplot as plt

from modules.boolean import boolean
from modules.AuB import AuB
from modules.AandB import AandB
from modules.AxB import AxB
from modules.AminusB import AminusB
from modules.notA import notA
from modules.sort.QuickSort import quick_sort
from modules.sort.MergeSort import merge_sort
from modules.sort.SelectionSort import selection_sort
from modules.sort.InsertionSort import insertion_sort
from modules.sort.ShellSort import shell_sort
from modules.sort.BubbleSort import bubble_sort

def printStartLine():
    print("\n")
    for i in range(16):
        print("= ", end = "")
    print()

def getRandArr(arr, a, b):
    for i in range(len(arr)):
        arr[i] = (int) ( random.uniform(a, b) )
    return arr

# = = = = = vars:

U = [1,2,3,4,5,6,7,8,9,10,11]
A = [1,3,4,7]
B = [3,5,6,7,8]
C = [2,4,5,7]

# = = = = = main():

# = = = = = Task 1
printStartLine()
print("Task 1. Boolean: P(A) - ?\n")
boolean(U, A)

# = = = = = Task 2
printStartLine()
print("Task 2. Merge sort. A u B - ?\n")

task2Arr4Merge = []
for i in range(12):
    task2Arr4Merge.append(0)
task2Arr4Merge = getRandArr(task2Arr4Merge, -100, 100)
print(task2Arr4Merge)
task2Arr4Merge = merge_sort(task2Arr4Merge)
print(task2Arr4Merge)
print()

arrTask2 = AuB(U, A, B)
print("%a u %a = %a" % (A, B, arrTask2))

# = = = = = Task 3
printStartLine()
print("Task 3. A ^ B - ?\n")
arrTask3 = AandB(U, A, B)
print("%a ^ %a = %a" % (A, B, arrTask3))

# = = = = = Task 4
printStartLine()
print("Task 4. A x B - ? |A x B| - ?\n")
AxB(A, B)

# = = = = = Task 5
printStartLine()
print("Task 5. A ^ ne (B\\C) - ?\n")

BminusC = AminusB(U, B, C)
print("%a \\ %a = %a\n" % (B, C, BminusC))

neBminusC = notA(U, BminusC)
print("not %a = %a\n" % (BminusC, neBminusC))

A_and_neBminusC = AandB(U, A, neBminusC)
print("%a ^ %a = %a\n" % (A, neBminusC, A_and_neBminusC))

# = = = = = Task 8.
printStartLine()
print("Task 8. Grey code\n")

for i in range(32):
    n = i
    code = ''
    while n > 0:
        code = str(n % 2) + code
        n = n // 2

    n = i ^ (i >> 1)
    GreyCode = ''
    while n > 0:
        GreyCode = str(n % 2) + GreyCode
        n = n // 2

    print("%4d - %8s | %4d - %8s" % (i, code, i ^ (i >> 1), GreyCode))

# = = = = = Task 9
printStartLine()
print("Task 9. Sort arr\n")

print("| %12s | %12s | %12s | %12s | %12s | %12s | %12s |" % (
    "n",
    "Quick",
    "Merge",
    "Selection",
    "Insertion",
    "Shell",
    "Bubble"
))

print("| %12s | %12s | %12s | %12s | %12s | %12s | %12s |" % (
    "------------",
    "------------",
    "------------",
    "------------",
    "------------",
    "------------",
    "------------"
))

step = 1000
while step <= 9000:
    arr = []

    for i in range(step):
        arr.append(0)

    print("| %12d " % step, end = "")

    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-b')
  
    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    arr = merge_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-g')

    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-r')

    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-c')

    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    shell_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-m')

    arr = getRandArr(arr, -100, 100)
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    print("| %12lf " % (end_time - start_time), end = "")
    plt.plot(step, end_time - start_time, 'o-y')
 
    print("|")
    step += 1000

plt.plot(0, 0, 'o-b', label="Quick sort")
plt.plot(0, 0, 'o-g', label="Merge sort")
plt.plot(0, 0, 'o-r', label="Selection sort")
plt.plot(0, 0, 'o-c', label="Insertion sort")
plt.plot(0, 0, 'o-m', label="Shell sort")
plt.plot(0, 0, 'o-y', label="Bubble sort")

plt.legend()
plt.show()
