def recurrent_variant6(n):
    if n == 0:
        return 0
    elif n == 1:
        return 5
    else:
        return 9 * recurrent_variant6(n - 1) - 20 * recurrent_variant6(n - 2)