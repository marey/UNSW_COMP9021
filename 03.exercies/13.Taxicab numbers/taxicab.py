# Written by Eric Martin for COMP9021


from math import pow


def taxicab(n, starting_from=2):
    solutions = [None] * n
    target = starting_from
    # Number of solutions found so far; should eventually reach n.
    m = 0
    while m < n:
        m = 0
        target += 1
        # Let a_cube be i ** 3 with i = 1, 2, 3...
        # If target - a_cube is also a cube,
        # then we have one decomposition of target
        # as a sum of two cubes.
        i = 1
        a_cube = 1
        while a_cube < target // 2:
            j = round(pow(target - a_cube, 1 / 3))
            if a_cube + j ** 3 == target:
                solutions[m] = (i, j)
                m += 1
            if m == n:
                break
            i += 1
            a_cube = i ** 3
    print(f'The smallest integer greater than', starting_from,
          'that can be written'
         )
    print(f'in {n} different ways as the sum of two cubes is {target}:')
    for m in range(n):
        print(f'  {target} = {solutions[m][0]}^3 + {solutions[m][1]}^3')
