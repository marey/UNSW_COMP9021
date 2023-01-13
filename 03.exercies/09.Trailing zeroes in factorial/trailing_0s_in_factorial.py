# Written by Eric Martin for COMP9021


from math import factorial


def first_computation(x):
    print(f'Computing the number of trailing 0s in {x}! '
          'dividing by 10 long enough...'
         )
    x = factorial(x)
    nb_of_trailing_0s = 0
    while x % 10 == 0:
        nb_of_trailing_0s += 1
        x //= 10
    return nb_of_trailing_0s

def second_computation(x):
    print(f'Computing the number of trailing 0s in {x}! '
          'by conversion to a string...'
         )
    x = str(factorial(x))
    for i in range(1, len(x) + 1):
        if x[-i] != '0':
            return i - 1

def third_computation(x):
    print(f'Computing the number of trailing 0s in {x}! the smart way...')
    nb_of_trailing_0s = 0
    power_of_five = 5
    while x >= power_of_five:
        nb_of_trailing_0s += x // power_of_five
        power_of_five *= 5
    return nb_of_trailing_0s
