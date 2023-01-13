# Written by Eric Martin for COMP9021


from math import sqrt


def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


print('The solutions are:\n')
# The list of all even i's such that a + i is one of
# a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
for a in range(10_001, 100_000 - good_leaps[-1], 2):
    # i should be in good_leaps iff a + i is prime
    # for i = 0, 2, 4, ..., 30.
    if all(((i in good_leaps) == is_prime(a + i))
               for i in range(0, good_leaps[-1] + 1, 2)
          ):
        print(' '.join((str(a + i) for i in good_leaps)))
