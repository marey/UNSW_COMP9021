# Written by Eric Martin for COMP9021


def colombo(n):
    sequence = [1, 2, 2]
    i = 3
    while n > len(sequence):
        sequence.extend([i] * sequence[i - 1])
        i += 1
    return sequence[: n]
