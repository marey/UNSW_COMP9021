from functools import reduce
from itertools import cycle
from operator import xor
from random import choice, randrange, seed
import sys

# POSSIBLY DEFINE FUNCTIONS HERE

try:
    piles = [int(n) for n in input('Describe the piles: ').split()]
    if any(n < 0 for n in piles):
        raise ValueError
except ValueError:
    print('Incorrect description, giving up!')
# INSERT YOUR CODE HERE
