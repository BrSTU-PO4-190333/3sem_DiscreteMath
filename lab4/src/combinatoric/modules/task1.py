def task1():
    print('Числа от 1 до 1001 деляющих на 2, на 3 и на 5:')
    sum = 0
    for i in range(1, 1001 + 1):
        if (i % 2 == 0) and (i % 3 == 0) and (i % 5 == 0):
            print(i, end = ' ')
            sum += 1
    print('\nКоличество: %d' % sum)