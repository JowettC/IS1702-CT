def sum_of_digits(i):
    if i < 10:
        return i
    return i % 10 + sum_of_digits(i//10)


