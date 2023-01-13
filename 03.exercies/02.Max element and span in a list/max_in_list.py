from random import seed, randint
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
L = [randint(0, 99) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
# Computes the maximum element of the list without using the
# builtin max().
max_element = 0
for e in L:
    if e > max_element:
        max_element = e
# Prints out the value of the maximum element within text out.
print('\nThe maximum number in this list is:', max_element)
# Confirms the value with the builtin max().
print('Confirming with builtin operation:', max(L))
