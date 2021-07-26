def recurrent_variant5(n):
    if n == 0:
        return 2
    elif n == 1:
        return 6
    else:
        return -2 * recurrent_variant5(n-1) - recurrent_variant5(n-2)