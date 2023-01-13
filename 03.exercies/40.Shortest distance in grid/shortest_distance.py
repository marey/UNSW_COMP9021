# Written by Eric Martin for COMP9021


from itertools import chain
from math import hypot


grid = []
with open('grid.txt') as file:
    for line in file:
        grid.append([int(x) for x in line.split()])
print('Here is the grid:\n')
for line in grid:
    print('', ''.join({0: '\N{White Large Square}',
                       1: '\N{Black Large Square}'
                      }[e] for e in line
                     )
         )
print()
height = len(grid)
width = len(grid[0])
solutions = set()
max_distance = 0
for i1 in range(height):
    for j1 in range(width):
        if not grid[i1][j1]:
            continue
        for (i2, j2) in chain(((i1, j) for j in range(j1 + 1, width)),
                              ((i, j) for i in range(i1 + 1, height)
                                          for j in range(width)
                              )
                             ):
            if not grid[i2][j2]:
                continue
            distance = hypot(i2 - i1, j2 - j1)
            if distance == max_distance:
                solutions.add(((j1 + 1, i1 + 1), (j2 + 1, i2 + 1)))
            elif distance > max_distance:
                max_distance = distance
                solutions = {((j1 + 1, i1 + 1), (j2 + 1, i2 + 1))}
print('The maximum distance between 2 points in the grid is:',
      round(max_distance, 2)
     )
print("That distance is between the following pairs of points:")
print('\n'.join(f'({j1}, {i1}) -- ({j2}, {i2})'
                    for ((j1, i1), (j2, i2)) in sorted(solutions)
               )
     )
