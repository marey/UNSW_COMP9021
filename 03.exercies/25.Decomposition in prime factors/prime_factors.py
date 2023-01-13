from collections import defaultdict
from math import sqrt


def prime_factors_of(n):
    if n < 2:
        return
    factors = defaultdict(int)
    rest = n
    while not rest % 2:
        rest //= 2    
        factors[2] += 1
    potential_factor = 1
    while rest > 1:
        try:
            upper_bound = round(sqrt(rest))
        # We could implement our own square root function to work on
        # integers, but if n is massively large, then our only hope is
        # that its prime decomposition consists of not too large primes
        # with high multiplicities, hence it is not worth bothering.
        # Bounding the search for prime factors at most equal to the
        # square root of rest is only valuable if the greatest prime
        # factor of rest is large (though of course not excessively so)
        # and significantly larger than the second greatest prime factor
        # of n.
        except OverflowError:
            upper_bound = rest
        while (potential_factor := potential_factor + 2) <= upper_bound:
            if not rest % potential_factor:
                while not rest % potential_factor:
                    rest //= potential_factor
                    factors[potential_factor] += 1
                break
        # No factor at most equal to upper_bound was found for rest,
        # hence rest is prime.
        else:
            factors[rest] = 1
            rest = 1
    print(n, '=', ' x '.join(f'{factor}^{e}' if e > 1 else f'{factor}'
                                 for (factor, e) in factors.items()
                            )
         )
