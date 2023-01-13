# Written by Eric Martin for COMP9021


from itertools import product
from operator import add
from random import choice

import matplotlib.pyplot as plt


def generate_random_walk(length=50_000):
    possible_moves = [p for p in product(range(-4, 5), repeat=2)
                          if p != (0, 0)
                     ]
    walk = [(0, 0)]
    for _ in range(length):
        move = choice(possible_moves)
        walk.append(tuple(map(add, walk[-1], move)))
    return walk
    

random_walk = generate_random_walk()
plt.figure(dpi=220, figsize=(5, 3))
plt.scatter(*tuple(zip(*random_walk)), c=tuple(range(len(random_walk))),
            cmap=plt.cm.Blues, edgecolor='none', s=1
           )
plt.scatter(*random_walk[0], c='green', edgecolors='none', s=10)
plt.scatter(*random_walk[-1], c='red', edgecolors='none', s=10)
plt.axis('off')
plt.show()
