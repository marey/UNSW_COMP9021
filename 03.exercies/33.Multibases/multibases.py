## Written by Eric Martin for COMP9021


def max_number_for(multibase):
    max_number = 0
    b = 1
    for i in range(1, len(multibase) + 1):
        max_number += b * (multibase[-i] - 1)
        b *= multibase[-i]
    return max_number

def conversion_to_base_10(n, *, multibase):
    digits = [int(e) for e in str(n)]
    if len(digits) > len(multibase)\
       or any(digits[-i] >= multibase[-i] for i in range(1, len(digits) + 1)):
        return
    b = multibase[-1]
    base_10_representation = digits[-1]
    for i in range(2, len(digits) + 1):
        base_10_representation += b * digits[-i]
        b *= multibase[-i]
    return base_10_representation

def conversion_to_multibase(n, *, multibase):
    bases = list(reversed(multibase))
    powers = [multibase.pop()] if len(multibase) > 1 else []
    while len(multibase) > 1:
        powers.append(powers[-1] * multibase.pop())
    multibase_representation = 0
    try:
        for _ in range(len(powers)):
            power = powers.pop()
            d = n // power
            if d >= bases.pop():
                raise IndexError
            multibase_representation = multibase_representation * 10 + d
            n %= power
        if n >= bases.pop():
            raise IndexError
        multibase_representation = multibase_representation * 10 + n
    except IndexError:
        return
    return multibase_representation
