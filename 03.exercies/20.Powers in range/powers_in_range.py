## Written by Eric Martin for COMP9021


from math import log, ceil


m, n = (int(x) for x in input('Input two positive integers: ').split())
solutions = set()
base = 2
while base ** 2 <= n:
    power = ceil(log(m, base))
    # For the case where log(m, base) is an integer,
    # but floating point computation overshoots it.
    if base ** (power - 1) >= m:
        power -= 1
    k = base ** power
    while k <= n:
        solutions.add((k, base, power))
        power += 1
        k = base ** power
    base += 1
solutions = sorted(solutions)
if solutions:
    field_width = len(str(max(k for (k, _, _) in solutions)))
for (k, base, power) in solutions:
    print(f'{k:{field_width}} = {base}^{power}')
