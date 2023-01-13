# Written by Eric Martin for COMP9021


from collections import defaultdict, namedtuple
from functools import reduce
from itertools import product
from operator import mul, itemgetter


def make_hasse_diagram(n):
    prime_factors = {}
    p = 2
    while n != 1:
        if n % p == 0:
            k = 1
            while n % p == 0:
                n //= p
                k += 1
            # prime_factors[p] is 1 + p's multiplicity in n
            prime_factors[p] = k
        p += 1
    factors = {1: '1'}
    edges = {p: set() for p in prime_factors}
    vertices = defaultdict(lambda: (set(), set()))
    vertices[1][1].update(prime_factors)
    possible_powers = product(*(range(i) for i in prime_factors.values()))
    # Discard (0, ..., 0): 1 is special
    next(possible_powers)
    for powers in possible_powers:
        factor = reduce(mul, (p ** m for (p, m) in zip(prime_factors, powers)))
        factors[factor] = 'x'.join(m == 1 and str(p)
                                   or '^'.join((str(p), str(m)))
                                       for (p, m) in zip(prime_factors, powers)
                                           if m
                                  )
        for (p, m) in filter(itemgetter(1), zip(prime_factors, powers)):
            smaller_factor = factor // p
            edges[p].add((smaller_factor, factor))
            vertices[smaller_factor][1].add(factor)
            vertices[factor][0].add(smaller_factor)
    sorted_factors = sorted(factors)
    return namedtuple('HasseDiagram',
                      ['factors', 'edges', 'vertices']
                     )({factor: factors[factor] for factor in sorted_factors},
                       {p: sorted(edges[p]) for p in prime_factors},
                       {v: (sorted(vertices[v][0]), sorted(vertices[v][1]))
                               for v in sorted_factors
                       }
                      )
