from random import seed, randrange
import sys


# Prompts the user for an integer to provide as argument to the
# seed() function.
try:
    arg_for_seed = int(input('Feed the seed with an integer: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
# Prompts the user a strictly positive number, nb_of_elements.
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
# Generates a list of nb_of_elements random integers between 0 and 99.
L = [randrange(100) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:' , L)
print()
# Computes the number of elements equal to 0, 1, 2 3 modulo 4.
# - remainders_modulo_4[0] to record the number of elements
#   equal to 0 modulo 4,
# - remainders_modulo_4[1] to record the number of elements
#   equal to 1 modulo 4,
# - remainders_modulo_4[2] to record the number of elements
#   equal to 2 modulo 4,
# - remainders_modulo_4[3] to record the number of elements
#   equal to 3 modulo 4.
remainders_modulo_4 = [0] * 4
for e in L:
    remainders_modulo_4[e % 4] += 1
# Prints those numbers within some text out.
for i in range(4):
    if remainders_modulo_4[i] == 0:
        print('There is no element', end=' ')
    elif remainders_modulo_4[i] == 1:
        print('There is 1 element', end=' ')
    else:
        print(f'There are', remainders_modulo_4[i], 'elements', end=' ')
    print('equal to', i, 'modulo 4.')
