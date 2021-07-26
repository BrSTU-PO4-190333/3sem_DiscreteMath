# чтение с файла
f = open('input.txt', 'r')
string = f.readline()
f.close()

# получаем число с файла в виде чила
N = int(string)

# функция, которая будет проверять есть ли повторяющие цифры в числе
def thereAreReplaces(N):
    string = str(N)

    arr = []
    for i in range(10):
        arr.append(0)

    for i in string:
        arr[int(i)] += 1

    # Если в массиве счетчик насчитал цифр больше 1, то возвратить True
    for i in arr:
        if i > 1:
            return True
    return False

# ищем число
k = 1 # для того, чтобы сделать операций сколько дано в условии
i = 1 # для итерация, чтобы знать какое сейчас число
while k <= N:
    if not thereAreReplaces(i):
        k += 1
    i += 1

# запись в файл
f = open('output.txt', 'w')
f.write(str(i - 1))
f.close()
